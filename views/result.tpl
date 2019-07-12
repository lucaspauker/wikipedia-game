<h1> Shortest path between <i>{{start}}</i> and <i>{{end}}</i>:</h1>

<ul>
  % for item in results:
    <li><a href={{item}}>{{item}}</a></li>
  % end
</ul>

<a href="/">Back</a>
