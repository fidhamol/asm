$(function () {

    "use strict";

	$("#main-menu li").hover(function() {
		$(this).find("ul").addClass("show");
	},function(){
		$(this).find("ul").removeClass("show");
		});
    


});


jQuery(document).ready(function() {
	
	if (jQuery('.remove-row-class').length) {
		jQuery('.remove-row-class').each(function(){
			//jQuery(this).children(".container").removeClass("container");
			jQuery(this).children(".container").children(".row").removeClass("row");
		});
		
		
	}
	
	if (jQuery('.remove-container-class').length) {
		jQuery('.remove-container-class').each(function(){
			jQuery(this).children(".rm-container-class").removeClass("container");
			jQuery(this).children(".rm-container-class").addClass("container-fluid");
		});
		
	}
	
	
	
	//Set subtitle
	if (jQuery('.section').length) {
		jQuery('.section').each(function(){
			
			if(jQuery(this).attr("data-sub-title")){
				var subtitle = jQuery(this).attr("data-sub-title");
			
				if (subtitle !== ''){
					jQuery(this).find(".subtitle-section").html(subtitle);
				}
			}else{
				jQuery(this).find(".subtitle-section").hide();
			}
			
			if(jQuery(this).attr("data-title")){
				var dttitle = jQuery(this).attr("data-title");
			
				if (dttitle !== ''){
					jQuery(this).find(".title-section").html(dttitle);
				}
			}
			
			//desction section 
			if(jQuery(this).attr("data-block-desc")){
				var desc_section = jQuery(this).attr("data-block-desc");
			
				if (desc_section !== ''){
					jQuery(this).find(".desc-section").html(desc_section).show();
					
				}
			}
			
			
		});
		
	}
	
	
});
 /* ===============================  justifiedGallery  =============================== */

    $('.justified-gallery').justifiedGallery({
        rowHeight: 400,
        lastRow: 'nojustify',
        margins: 15
    });
