;(function ($){
  $(function() {
    // Main menu mobile button click
    $('.mobile-menu-button').click(function() {
      $('.main-menu').toggleClass('open');
    });

    // Watch List functionality
    $('.js-watchlist-add').click(function() {
      var url = $(this).data('href');
      var self = $(this);
      $.get( url, {} )
        .done(function(data) {
          self.hide();
          self.siblings('.js-watchlist-remove').show();
        });
    })

    $('.js-watchlist-remove').click(function() {
      var url = $(this).data('href');
      var self = $(this);
      $.get( url, {} )
        .done(function(data) {
          self.hide();
          self.siblings('.js-watchlist-add').show();
          if (self.data('remove')) {
            self.closest('.offering-content-listing').remove();
          }
        });
    })
  });
})(jQuery);
