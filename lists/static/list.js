/**
 * Created by chn_t on 2017/1/30.
 */


window.Superlists = {};
window.Superlists.initialize = function () {
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
  });
};