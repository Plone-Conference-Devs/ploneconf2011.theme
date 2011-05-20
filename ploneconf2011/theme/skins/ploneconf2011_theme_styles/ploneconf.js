(function($) { $(function() {
   jq("#portal-globalnav li").hover(
     function() { jq(this).addClass("hover"); },
     function() { jq(this).removeClass("hover"); }
   );
}); })(jQuery);