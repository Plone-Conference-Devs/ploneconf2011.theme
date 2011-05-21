(function($) { $(function() {
   jq("#portal-globalnav li").hover(
     function() { jq(this).addClass("hover"); },
     function() { jq(this).removeClass("hover"); }
   );

   jq("ul.thumb li").hover(function() {
	jq(this).css({'z-index' : '10'}); /*Add a higher z-index value so this image stays on top*/ 
	jq(this).find('div').addClass("hover").stop() /* Add class of "hover", then stop animation queue buildup*/
		.animate({
			marginTop: '-100px', /* The next 4 lines will vertically align this image */
			marginLeft: '-110px'
		}, 200); /* this value of "200" is the speed of how fast/slow this hover animates */

	} , function() {
	jq(this).css({'z-index' : '0'}); /* Set z-index back to 0 */
	jq(this).find('div').removeClass("hover").stop()  /* Remove the "hover" class , then stop animation queue buildup*/
		.animate({
			marginTop: '0', /* Set alignment back to default */
			marginLeft: '0'
		}, 400);
});

}); })(jQuery);