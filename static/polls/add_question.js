jQuery(function($) {
var i = 0;
$("#create_answer").click(function() {
  if ($('#question_input').val() != '') {
    $('#create_question_requirement_2').css('display', 'none');
    if ($('#answer_a').val() != '') {
      if ($('#answer_b').val() != '') {
        if (i < 3) {
          $('#create_question_requirement_1').css('display', 'none');
          $("ul > li:last-child").after('<li class="list-group-item"><label>answer:</label> <input class="answer" type="text" name="answer_' + String(i) + '"></input><i id="remove_answer" class="float-right fas fa-times-circle"></i></li>');
          $('#submit')[0].scrollIntoView();
          i += 1;
          return false;
        }
        else {
          $('#create_question_requirement_0').css('display', 'inline');
        }
      }
      else {
        $('#create_question_requirement_1').css('display', 'inline');
      }
    }
    else {
      $('#create_question_requirement_1').css('display', 'inline');
    }
  }
  else {
    $('#create_question_requirement_2').css('display', 'inline');
  }
});

$('#question_input').change(function() {
  if ($('#question_input').val() == '') {
    alert('here');
    $('#submit').prop('disabled', true);
  }
  else {
    $('#submit').prop('disabled', false);
  }
});



$(document).on('click', '#remove_answer', function() {
  $(this).parent().remove();
  i -= 1;
});















})(jQuery);
