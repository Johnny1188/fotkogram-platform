// Create disable and enable scrolling functions:
function disableScrolling() {
    var x=window.scrollX;
    var y=window.scrollY;
    window.onscroll=function(){window.scrollTo(x, y);};
}
function enableScrolling(){
    window.onscroll=function(){};
}

// Create function to transfer the invisible form from home.html to the modal form container:
function move_form(post_id) {
    var comment_form = document.getElementById(post_id+"_form").innerHTML;
    comment_form_modal_container.innerHTML = comment_form;
    comment_form_modal_container.firstElementChild.style.display = "block";
}

// Get all the variables from modal:
var modal = document.getElementById('modal_window');
var modal_box = document.getElementById('modal_box');
var comment_form_modal_container = document.getElementById("form_container");
var modal_box_text_space = document.getElementById("modal_box_text");
var cross_icon = document.getElementById("cross_icon_container");
cross_icon.addEventListener("click", function() {
    modal.style.visibility = "hidden";
    enableScrolling();
})

// Add click-event to all posts on the home page and show modal on click:
var posts = document.getElementsByClassName('post');
for (let i = 0; i < posts.length; i++) {
    posts[i].addEventListener("click", function(){
        // Get the post id from the end of its ID and disable scrolling:
        var post_id = posts[i].id;
        disableScrolling();
        // Get the form from home.html and put it inside the form_container in the modal:
        move_form(post_id);
        // Show the modal box:
        modal.style.visibility = "visible";
        // Get the clicked image and insert it into the modal_box:
        var image_to_show_in_html = document.getElementById(post_id + "_post_image").innerHTML;
        modal_box.firstElementChild.innerHTML = image_to_show_in_html;
        // Get the text of the post and display it in the modal box <p> tag:
        var text_to_show_in_html = document.getElementById(post_id + "_post_text").firstElementChild;
        modal_box_text_space.textContent = text_to_show_in_html.textContent;
    });
}

// Commenting function:
var comment_post_button = document.getElementsByClassName("comment");
for (let i = 0; i < comment_post_button.length; i++) {
    comment_post_button[i].addEventListener("click", function(){
        var post_id_without_letters = comment_post_button[i].id.split("_");
        var post_id = post_id_without_letters[0];
        // Get the form from home.html and put it inside the form_container in the modal:
        move_form(post_id);
        // Show the modal box:
        disableScrolling();
        modal.style.visibility = "visible";
        var image_to_show_in_html = document.getElementById(post_id + "_post_image").innerHTML;
        modal_box.firstElementChild.innerHTML = image_to_show_in_html;
        // Get the text of the post and display it in the modal box <p> tag:
        var text_to_show_in_html = document.getElementById(post_id + "_post_text").firstElementChild;
        modal_box_text_space.textContent = text_to_show_in_html.textContent;
    })
}

// Create function for pagination
//      - put away the pages' numbers
//      - while scrolling, load the next page