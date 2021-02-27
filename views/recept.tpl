% rebase('bootstrap.tpl')
% if recept is None:
  <h3>Trenutno ni odprtega recepta</h3>
% else:
  <h3 class="poudari">{{ recept.naslov_recepta }}</h3>
  <span class="text-light bg-dark">
      {{ recept.stevilo_glasov() }} glasov
  </span>
    <form action="/glasuj/{{ recept.indeks_recepta }}" method="POST">
       <input class="btn btn-dark" type="submit" value="glasuj">
    </form>
  <ul class="list-group">
  % for indeks_sestavine, sestavina in enumerate(recept.seznam_sestavin):
  <li class="list-group-item">
    {{ sestavina.besedilo }}
  </li>
  % end
  <form action="/recept" method="POST">
    Ime: <input type="text" name="komentator">
    <textarea rows="5" cols="30" name="komentar" class="mb-1">Ddodaj komentar</textarea><br>
     <input class="btn btn-dark" type="submit" value="Komentiraj">
  </form>
    % for komentar in recept.komentarji:
    <li class="list-group-item">
    {{ komentar.ime }} , {{ komentar.besedilo }}
  </li>
    % end
  % end


