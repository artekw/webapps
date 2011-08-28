<p>ALL:</p>
<table border="1">
%for row in rows:
	<tr>
	%for r in row:
		<td><img src=/upl/{{r}}.jpg></td>
	%end
	</tr>
%end
</table>