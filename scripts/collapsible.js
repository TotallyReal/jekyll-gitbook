
// Get all elements with the class 'title'
var titles = document.querySelectorAll('.callout-title[collapsible]');

console.log('number of titles is '+titles.length);

// Iterate over each title
titles.forEach(function(title) {
    console.log(title);
  // Add click event listener
  title.addEventListener('click', function() {
    console.log('pressed '+this);
    // Toggle the 'collapsed' attribute on the content element
    var content = this.nextElementSibling;
    console.log('content is  '+content);
    console.log('Content ID:', content.id);
console.log('Content Class:', content.className);
console.log('Content HTML:', content.outerHTML);
    if (content.hasAttribute('data-collapsed')) {
    console.log('removing attribute')
      content.removeAttribute('data-collapsed');
    } else {
    console.log('adding attribute')
      content.setAttribute('data-collapsed', '');
    }
  });
});