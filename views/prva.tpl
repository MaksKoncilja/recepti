% rebase('bootstrap.tpl')
% if seznam_receptov is None:
    <p>Ni receptov</p>
% else:
  <a href="/k" class="btn btn-dark">Razvrsti po kalorijah<a>
  <a href="/h" class="btn btn-dark">Razvrsti po času priprave<a>
  <div class="row mt-3"></div>
  <div class="card" style="width: 23rem;">
  <div class="card-header">
    <h4>Recepti</h4>
  </div>
  % for r in seznam_receptov:
    <div class="card mx-auto" style="width: 23rem;">
        <h5><a href="/recept/{{ r.indeks_recepta }}"> {{ r.naslov_recepta }} <a></h5>
    </div>
  % end
% end