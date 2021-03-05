% rebase('bootstrap.tpl')
% if recept is None:
  <h3>Trenutno ni odprtega recepta</h3>
% else:
  <h3 class="poudari">{{ recept.naslov_recepta }}</h3>
  <div class="row mt-3"></div>
    <form action="/glasuj/{{ recept.indeks_recepta }}" method="POST">{{ recept.stevilo_glasov() }} glasov
       <input class="btn btn-secondary btn-sm" type="submit" value="glasuj">
    </form>
  <div class="row mt-3"></div>
  <p>Kalorijska vrednost: {{ recept.kalorijska_vrednost }} kal <br>
  Čas priprave: {{ recept.cas_priprave }} </p>
  <div class="row mt-3"></div>
  <h6>Sestavine</h6>
  <ul class="list-group" style="width: 23rem;">
  % for indeks_sestavine, sestavina in enumerate(recept.seznam_sestavin):
  <li>
    {{ sestavina.besedilo }}
  </li>
  % end
  <div class="row mt-3"></div>
  <h6>Postopek priprave</h6>
  <p>{{ recept.navodila }}</p>
  <div class="row mt-3"></div>
  <h6>Komentarji</h6>
    % for komentar in recept.komentarji:
    <li class="list-group-item" style="font-size:15px">
    {{ komentar.ime }} : {{ komentar.besedilo }}
    </li>
    % end
  <div class="row mt-3"></div>
  <form action="/recept" method="POST">
    Ime: <input type="text" name="komentator">
    <div class="row mt-3"></div>
    <textarea rows="5" cols="28" name="komentar" placeholder="Ddodaj komentar" class="mb-1"></textarea><br>
     <input class="btn btn-secondary btn-sm" type="submit" value="Komentiraj">
  </form>
  % end


