

    function newMessage() {
		$(".messages").animate({ scrollTop: $(document).height() }, "fast");

		var message = $(".message-input input").val();

		if($.trim(message) == '') {
		  return false;
		}
		$('<li class="sent"><img src="../static/images/ask.png" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
		$('.message-input input').val(null);
		$('<li class="replies" id ="loader"><img src="../static/images/loader.gif" alt="" width="1000"</li>').appendTo($('.messages ul'));

		$.ajax({
		  url: '/process',
		  type: 'POST',
		  dataType: 'application/json',
		  data: {text: message},
		  dataType: 'json',
		  success: function(response) {
			$('#loader').remove();
			var response_nom = response.nom;
			var response_adresse = response.adresse;
			var response_texte = response.texte;
			if (response_nom != undefined){
				$(".messages").animate({ scrollTop: $(document).height() }, "fast");
			  $('<li class="replies"><img src="../static/images/papy.png" alt="" /><p>' + response_nom + '</p></li>').appendTo($('.messages ul'));
			  $('<li class="replies"><img src="../static/images/papy.png" alt="" /><p>' + response_adresse + '</p></li>').appendTo($('.messages ul'));
			  $('<li class="replies"><img src="../static/images/papy.png" alt="" /><p>' + response_texte + '</p></li>').appendTo($('.messages ul'));
			$(`<li> <iframe width="425" height="250"frameborder="0" src="https://www.google.com/maps/embed/v1/place?key=AIzaSyBh_Oj3Rj_gosxQUQxEzeYE95DbixLTZ8g&q=${response_nom} + ${response_adresse}" allowfullscreen></iframe></li>`).appendTo($('.map_google ul'));
			

			}
			else{	
						
			  $('<li class="replies"><img src="../static/images/papy.png" alt="" /><p>' + response_texte + '</p></li>').appendTo($('.messages ul'));
			  $(".messages").animate({ scrollTop: $(document).height() }, "fast");

			}
		  }
		  });

  
	  };
  
	  $newItemForm = $('.message-input');
  
  
	  $newItemForm .on('submit', function(e) {
		e.preventDefault();
		newMessage();
	  });