document.addEventListener("DOMContentLoaded", function() {
  var path = window.location.pathname;
  var page = path.split("/");
  if (page[2] == 'award' && !(Number.isInteger(page[3]))) {
    document.querySelector("#id_kind").addEventListener('change', function() {
      showData();
    });
  };
});


function showData() {
  var selectedMaterial = document.querySelector("#id_kind").value;
  if (selectedMaterial == 'Movie') {
    document.querySelector("#label_id_selected").innerHTML = 'Movie:';
    createSelection(movieList, ".award-create-form", "#id_selected");
  } else if (selectedMaterial == 'Actor') {
    document.querySelector("#label_id_selected").innerHTML = 'Actor:';
    createSelection(actorList, ".award-create-form", "#id_selected");
  };
};


function getSelectTag(form, id_name) {
  var awardCreateForm = document.querySelector(form);
  var selectList = document.querySelector(id_name);
  selectList.innerHTML = "";
  return selectList
};


function createSelection(objects, form, select_id) {
  var selectList = getSelectTag(form, select_id)
  for (var object of objects) {
    console.log(object)
    var option = document.createElement("option");
    option.value = object[0];
    option.text = object[1];
    selectList.appendChild(option);
  }
};


function updateComment(returnUrl, id) {
  var commentForm = document.querySelector(".comment_form");
  var currentComment = document.querySelector("#comment-text" + id);
  var cloneCommentForm = commentForm.cloneNode(true);
  cloneCommentForm.querySelector('.form-control').value += currentComment.querySelector("p").innerText;
  cloneCommentForm.action = returnUrl;
  currentComment.innerHTML = "";
  currentComment.appendChild(cloneCommentForm);
};


function redirectHome() {
  var current_site = window.location.origin;
  location.replace(current_site);
}
