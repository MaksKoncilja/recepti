% rebase('bootstrap.tpl')
% if recept is None:
  <h3>Trenutno ni odprtega recepta</h3>
% else:
  <h3 class="poudari">{{ recept.naslov_recepta }}</h3>
  <span class="badge badge-light">
      {{ recept.stevilo_glasov() }} glasov
    </span>
    <form action="/glasuj/" method="POST">
       <input type="hidden" value="{{indeks_recepta}}" name="indeks_recepta">
       <input class="btn btn-light" type="submit" value="glasuj">
    </form>
  <ul class="list-group">
  % for indeks_sestavine, sestavina in enumerate(recept.seznam_sestavin):
  <li class="list-group-item">
    {{ sestavina.besedilo }}
  </li>
  % end
% end