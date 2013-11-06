$(function() {
	var slider = function(s) {
		this.$slider = $(s);
		this.$container = $('#gallery-container');
		this.$blocks = this.$container.children('.gallery-block');
		this.$prev = this.$slider.children('.nav.prev'); 
		this.$next = this.$slider.children('.nav.next');
		this.slide = {
			value: 600,
			time: 250,
		}
		this.gallery_index = 0;
		this.init();
	}
	slider.prototype = {
		init: function() {
			this.$next.click($.proxy(this.next_block,this));
			this.$prev.click($.proxy(this.prev_block,this));
		},
		prev_block: function() {
			if (this.$blocks[this.gallery_index-1]){
				this.gallery_index--;
				this.slide_block(true);
			}
		},
		next_block: function() {
			if (this.$blocks[this.gallery_index+1]){
				this.gallery_index++;
				this.slide_block(false);
			}
		},
		slide_block: function(slide_left) {
				var value = (slide_left ? "+=" : "-=") + this.slide.value;
				this.$container.animate({
					left: value,
				},this.slide.time,$.proxy(function() {
						this.toggle_nav();
					},this)
				);
		},
		toggle_nav: function() {
			if (!this.$blocks[this.gallery_index-1])
				this.$prev.hide();
			else
				this.$prev.show();
			if (!this.$blocks[this.gallery_index+1])
				this.$next.hide();
			else
				this.$next.show();
		},
	}
	$('#rotator').each(function() {
		new slider(this);
	})
});