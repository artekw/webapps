<title>pyimgshare</title>
<link rel="stylesheet" type="text/css" href="style/styl.css" />
<div id="wrap">
<div id="box">
<table boarde="0"><tr>
%for p in pages:
	<td><a href="http://192.168.88.245:5000/{{p}}"><img title="{{p}}" src="/style/{{p}}.png"></a></td>
%end
</div>
<tr></table>
</div>
Napisane w bottlepy