/* If you've ever had the need to link directly to an open modal window with Bootstrap, here's a quick and easy way to do it:

Make sure your modal has an id:

<div class="modal" id="myModal" ... >

Then stick this bit of Javascript at at the end of your document:
 */

$(document).ready(function() {

  if(window.location.href.indexOf('#myModal') != -1) {
    $('#myModal').modal('show');
  }

});

/*
Then you can send people to http://www.website.com/page.html#myModal and it'll load the page with the modal open.
*/