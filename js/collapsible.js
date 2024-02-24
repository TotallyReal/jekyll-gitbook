
var callouts = document.querySelectorAll('.callout[collapsible]');
for (let calloutElement of callouts){
    var title = calloutElement.querySelector(".callout-title");
    //console.log(title);

    title.addEventListener('click', function() {
        var state = calloutElement.getAttribute('collapsible');
        var new_state = (state == 'hide') ? 'show' : 'hide';
        calloutElement.setAttribute('collapsible', new_state);
    });
}

