
// Get all elements with the class 'title'
var titles = document.querySelectorAll('.callout-title[collapsible]');

// Iterate over each title
titles.forEach(function(title) {
  // Add click event listener
  title.addEventListener('click', function() {
    // Toggle the 'collapsed' attribute on the content element
    var content = this.nextElementSibling;
    if (content.hasAttribute('data-collapsed')) {
      content.removeAttribute('data-collapsed');
    } else {
      content.setAttribute('data-collapsed', '');
    }
  });
});