function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("id", ev.target.id);
  ev.dataTransfer.setData("dragged_element",ev.target); 
  ev.dataTransfer.setData("text", ev.target.innerHTML);
  ev.dataTransfer.setData("isAnswer","yes");
}

function update_answer_input(target) {
    var wrapper=findAncestor(target,"ex-wrapper");
    var answer_cells=wrapper.getElementsByClassName("drag-n-drop-aswer-cell");
    var answer_el=wrapper.getElementsByClassName("dragndrop-widget");
    var out = ""
    var answers = []
    for (i=0;i<answer_cells.length;i=i+1) {
      out+=i + answer_cells[i].innerHTML + " "
      answers.push(answer_cells[i].innerHTML)
    }
    answer_el[0].setAttribute("value",answers.join(" "))  
    //answer_el[0].innerHTML=answers.join(" ")  
    //alert(out)
    console.log(answer_el)
    
}

function get_id(id) {
  id_to_return=id.substring(7); //7 because it trims first 7 chars of "answer-459nvf-..." to get an id
  return id_to_return; 
}

function drag_answer(ev) {
  //ev.dataTransfer.setData("id")="";     
  ev.dataTransfer.setData("id", ev.target.id);
  ev.dataTransfer.setData("class_name",ev.target.id);
  ev.dataTransfer.setData("text", ev.target.innerHTML);
  ev.dataTransfer.setData("isAnswer","no");
}


function remove_element(element) {
    
  id=get_id(element.id);
  //alert("a" + element.id + "a");
  choice_element=document.getElementById(id);
  choice_element.style.display="";
  
  element.innerHTML="";
  element.removeAttribute("id");
  update_answer_input(element)
  
}

function findAncestor(el, cls) {
  while ((el = el.parentElement) && !el.classList.contains(cls));
  return el;  
}


function add_answer(ev) {
  //var answer_cells=document.getElementsByClassName("drag-n-drop-answers-wrapper");
  //var answer_cells=ev.target.closest("ex-wrapper");
  var wrapper=findAncestor(ev.target,"ex-wrapper");
  var answer_cells=wrapper.getElementsByClassName("drag-n-drop-aswer-cell");
  var out = ""
  for (i=0;i<answer_cells.length;i=i+1) {
      if (!answer_cells[i].id) {
            put_choice_in_answer(ev.target,answer_cells[i])
            update_answer_input(ev.target)
            return 0
      }
      out+=i + answer_cells[i].id + "\n"
  }
  

}

function check_if_dropped_empty(ev) {
    if (!ev.dataTransfer.getData("id")) {     
        return 0
    } else {
        return 1
    }

}

function drop(ev) {
    // requires: 
               
    if (!check_if_dropped_empty(ev)) { 
        //alert("Its empty !")
        remove_element(ev.target);    
        return 0;
    }
    
    var draggedId   = ev.dataTransfer.getData("id");
    //var draggedClassName   = ev.dataTransfer.getData("class_name");
    //alert(draggedId)
    var choice_grandpa_el = document.getElementById(draggedId).parentElement.parentElement
    //var choice_grandpa_el = dragged_element.parentElement.parentElement
    var answer_grandpa_el = ev.target.parentElement.parentElement
    //alert(choice_grandpa_el.className + " " +answer_grandpa_el.className)
    
    if (choice_grandpa_el.className != answer_grandpa_el.className) {
        alert("Hey !!! Don't mess around. You have tried to put an answer from different excersise")
        return 0
    }
    
    if (ev.dataTransfer.getData("isAnswer") == "yes") {
        choice_drop(ev)
    } else {
            answer_drop(ev)
        }
        
    update_answer_input(ev.target)     
}



function answer_drop(ev) {
  ev.preventDefault();
  var draggedId   = ev.dataTransfer.getData("id");
  var draggedText = ev.dataTransfer.getData("text");

  var dragged_element = document.getElementById(draggedId)
  var target_element   = ev.target 

  if (ev.target.id) {
      remove_element(ev.target)
      //
      //id=ev.target.id.substring(7) //7 because it trims first 7 chars of "answer-459nvf-..." to get an id
      //document.getElementById(id).style.display="";      
  }
    
  dragged_element.innerHTML="";
  dragged_element.removeAttribute("id");
  target_element.id=draggedId;
  target_element.innerHTML=draggedText;
  
}

function put_choice_in_answer(choice_el,answer_el) {
  answer_el.innerHTML=choice_el.innerHTML;
  answer_el.id="answer-" + choice_el.id
  choice_el.style.display="none"
}

function set_answer_id(id){
  return "answer-" + id 
}

function choice_drop(ev) {
  ev.preventDefault();
  var dataid   = ev.dataTransfer.getData("id");
  var datatext = ev.dataTransfer.getData("text");
  //alert(data)
  //alert(dataid + datatext)
  if (ev.target.id) {
      id=get_id(ev.target.id)
      document.getElementById(id).style.display="";  
  }
  ev.target.innerHTML=datatext;
  ev.target.id="answer-" + dataid
  document.getElementById(dataid).style.display="none";
  
  //window.alert(element);
}
