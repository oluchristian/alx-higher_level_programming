// Changes the color of the text in the `header` element to red when user
// clicks on the tag `div#red_header`
$('div#red_header').on('click', () => {
	$('header').css('color', '#FF0000');
  });