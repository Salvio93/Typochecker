const error_panel = document.querySelector("#error_panel");
const txt_modif = document.querySelector("#text_edit");

let previous_txt = null;


async function api_get(url) {
  let request = new Request(url, {
    method: "GET",
  });

  let ret = await fetch(request)
    .then((response) => {
      if (response.status === 200) {
        return response.json();
      } else {
      throw new Error("Something went wrong on API server!");
    }
  });

  return ret;
}


/*
  Edit
*/

// text content
update_content();
async function update_content() {

    let current_text = await api_get("api/get_text");
    let all_corrections = await api_get("api/get_all_corrections");

    txt_modif.value = current_text;
    previous_txt = current_text;
    
    let errors_html = "<ul>\n";
    
    for (let id in all_corrections) {
      let error = all_corrections[id]; 
      if (error && error["error"]["detected"]==0) errors_html += "<li onclick=\"error_hoverd("+ error["error"]["document_rule_id"] + ","+error["error"]["idx"]+ ");\" " +  
                     "<li onmouseout=\"error_not_hoverd("+ error["error"]["document_rule_id"] + ");\" "+">"
                     + error["rule"]["name"] + ' <button onclick="accept_chang_id(' + error["error"]["document_rule_id"] + ')"class="button"> v </button>'
                     + ' <button onclick="refuse_chang_id(' + error["error"]["document_rule_id"] + ')"class="button"> x </button>' +'</li>\n';
    }

    errors_html += "</ul>";

    error_panel.innerHTML = errors_html;
    handleInput()
}

async function update_errors() {
  let all_corrections = await api_get("api/get_all_corrections");
  
  let errors_html = "<ul>\n";
  
  for (let id in all_corrections) {
    let error = all_corrections[id]; 
    if (error && error["error"]["detected"]==0) errors_html += "<li onclick=\"error_hoverd("+ error["error"]["document_rule_id"] + ","+error["error"]["idx"]+ ");\" " +  
                   "<li onmouseout=\"error_not_hoverd("+ error["error"]["document_rule_id"] + ");\" "+">"
                   + error["rule"]["name"] + ' <button onclick="accept_chang_id(' + error["error"]["document_rule_id"] + ')"class="button"> v </button>'
                   + ' <button onclick="refuse_chang_id(' + error["error"]["document_rule_id"] + ')"class="button"> x </button>' +'</li>\n';
  }

  errors_html += "</ul>";

  error_panel.innerHTML = errors_html;
}

// change
async function accept_chang_id(rule_id) {
  await api_get("/api/accept_change_" + rule_id.toString()).then(()=>{ update_content();});
}

async function refuse_chang_id(rule_id) {
  await api_get("/api/refuse_change_" + rule_id.toString()).then(()=>{ update_content();});
}

async function end_review() {

  fetch("/api/end_review", {
    method: "POST",
    body: JSON.stringify(
      txt_modif.value
    ),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
    .then(()=>{window.location.href = "/rapport";})
}


/*
  Virtual keyboard
*/ 
document.addEventListener('DOMContentLoaded', function() {
  const copyableLetters = document.querySelectorAll('.copyable');
  copyableLetters.forEach(letter => {
      letter.addEventListener('click', function() {
          copyToClipboard(this.innerText);
      });
  });

  function copyToClipboard(text) {
      const textarea = document.createElement('textarea');
      textarea.value = text;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
      const letter = text;
      const message = 'Copiée : ' + letter;
      showAlert(message);
  }

  function showAlert(message) {
      const alertModal = document.getElementById('alertModal');
      const alertMessage = document.getElementById('alertMessage');
      alertMessage.textContent = message;
      alertModal.style.display = 'block';
      setTimeout(function() {
          alertModal.style.display = "none";
      }, 1000);
  }
  
});


/*
  Highlights
*/
var backdrop = document.querySelector('.backdrop');
var highlights = document.querySelector('.highlights');


async function applyHighlights(text) {
  let all_corrections = await api_get("api/get_all_corrections");
  if (all_corrections.lenght==0) {
    return;
  }

  let n_text = "";
  let idx=0;

  while (idx<text.length) {
    let error = null;

    for (let candidat_id in all_corrections) {
      let candidat = all_corrections[candidat_id];
      if (candidat["error"]["idx"] == idx){
        error = candidat;
        console.log(error)
      }
    }
    if (error == null) {
      n_text += text[idx];
      idx++;
      
    } else { 
      console.log('itération:"'+idx+'"')

      if(error["error"]["detected"]==0){
        n_text += '<mark id="err' + error["error"]["document_rule_id"] + '">' + error["rule"]["bad_typo"] + '</mark>';
      }
      else{
        console.log(error)

        n_text += '<mark id="err' + error["error"]["document_rule_id"] + '" style="background-color:#00ced1; color: black;">' + text.substring(idx,idx+error["error"]["lenght"]) + '</mark>';
        console.log(text.substring(idx,idx+error["error"]["lenght"]))
      }
      idx += error["error"]["lenght"];
    }
  }

  text = n_text.replace(/\n$/g, '\n\n');
    
  return text;
}

function handleInput() {
  
  var text = txt_modif.value;
  Promise.resolve(applyHighlights(text).then((response) => { highlights.innerHTML = response;} ));
}

function update_text() {
  fetch("/api/update_text", {
    method: "POST",
    body: JSON.stringify(
      txt_modif.value
    ),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
    .then(()=>{handleInput(); update_errors(); input_timer=null});
}

// update only aftre 1s of no typing
let input_timer = null;
function nonSpamHandleInput() {
  if (input_timer == null) {
    input_timer = setTimeout(update_text, 1000);
  } else {
    clearTimeout(input_timer);
    input_timer = setTimeout(update_text, 1000);
  }
}

function handleScroll() {
  var scrollTop = txt_modif.scrollTop;
  backdrop.scrollTop = scrollTop;
  
  var scrollLeft = txt_modif.scrollLeft;
  backdrop.scrollLeft = scrollLeft;  
}

function bindEvents() {
  txt_modif.addEventListener('input', nonSpamHandleInput, false);
  txt_modif.addEventListener('scroll', handleScroll, false); 
  txt_modif.addEventListener('keydown', function(e) {
    if (e.key == 'Tab') {
      e.preventDefault();
      var start = this.selectionStart;
      var end = this.selectionEnd;
  
      // set textarea value to: text before caret + tab + text after caret
      this.value = this.value.substring(0, start) +
        "\t" + this.value.substring(end);
  
      // put caret at right position again
      this.selectionStart =
        this.selectionEnd = start + 1;
        nonSpamHandleInput();
    }
  });
}

function error_hoverd(idx, pos) { 
  const char_y = 24;
  const max_char_per_l = 130;

  // find line
  let line = 0;
  let buffer = 0;

  let i=0;
  let text = txt_modif.value;
  while (i<pos) {
    if (text[i] == '\n') {
      buffer = 0;
      line++;
    } else {
      buffer++;
      if (buffer > max_char_per_l) {
        buffer =0; line++;
      }
    }
    i++;
  }

  txt_modif.scrollTop = (line-6)*char_y;
  let block = document.querySelector("#err"+idx.toString());
  block.className = "border-2 border-black";
}

function error_not_hoverd(idx) {
  let block = document.querySelector("#err"+idx.toString());
  block.className = "";
}

txt_modif.scrollTop = 0;
bindEvents();
handleInput();