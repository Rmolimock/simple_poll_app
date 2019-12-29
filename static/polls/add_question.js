jQuery(function($) {
var i = 0;
$("#create_choice").click(function() {
    $("ul > li:last-child").after('<li class="list-group-item"><label>Choice:</label> <input class="choice" type="text" name="choice_text' + String(i) + '"></input> <div class="btn btn-danger btn-sm remove_choice" id="remove_choice">X</div></li>');
$('#submit')[0].scrollIntoView();
i += 1;
return false;
});

$(document).on('click', '#remove_choice', function() {
  $(this).parent().remove();
});















})(jQuery);
