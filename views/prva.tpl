% rebase('bootstrap.tpl')
% if seznam_receptov is None:
    <p>Ni receptov</p>
% else:
  <a href="/k" class="btn btn-dark">Razvrsti po kalorijah<a>
  <a href="/h" class="btn btn-dark">Razvrsti po času priprave<a>
  % for r in seznam_receptov:
    <div class="card mx-auto" style="width: 18rem;">
        <h5><a href="/recept/{{ r.indeks_recepta }}"> {{ r.naslov_recepta }} <a></h5>
        <span>{{r.indeks_recepta}}</span>
    </div>
  % end
% end