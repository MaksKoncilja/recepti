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
% end


