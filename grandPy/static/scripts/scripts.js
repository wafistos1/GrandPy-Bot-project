

$(function() {
	
	var $list, $newItemForm;
	
	$list = $('ul');
	$newItemForm = $('#question');
	
	$newItemForm.on('submit', function(e) {
	  e.preventDefault();
	  var text = $('input:text').val();
	  add_text = '<li><div id="user">' + text + "</div><div><img src='../static/images/ask.png' width=\"50px\" ></div></li>"
	  $list.append(add_text);
	  $('input:text').val();
	  $.ajax({
		url: '/process',
		type: 'POST',
		dataType: 'application/json',
		data: {text: text},
		dataType: 'json',
		success: function(response) {
			
			var response_nom = response.nom;
			var response_adresse = response.adresse;
			var response_photo = response.photo;
			var response_texte = response.texte;
			if (response_nom != undefined){
				$list.append('<li id = "rep"><div><img src=\'../static/images/papy.png\' width=\"50px\" ></div><div>Si tu cherche '  + response_nom + " ??</div></li>");
				$list.append('<li = "rep"><div><img src=\'../static/images/papy.png\' width=\"50px\" ></div><div>Ben je crois qu\'elle se trouve: ' + response_adresse + "</div></li>");
				$list.append('<li = "rep"><div><img src=\'../static/images/papy.png\' width=\"50px\" ></div><div> Oh mon enfant!! cet endroit qui est: ' + response_texte + "</div></li>");
			}
			else{			
			$list.append('<li = "rep"><div><img src=\'../static/images/papy.png\' width=\"50px\" ></div><div> ' + response_texte + "</div></li>");
			}
		}
		});

		
	});


  
  	});
  

  

