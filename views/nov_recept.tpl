% rebase('bootstrap.tpl')
<form action="/dodaj/" method="POST">
    Naslov recepta: <input type="text" name="naslov_recepta" class="mb-1"><br>
    Seznam sestavin: <textarea rows="10" cols="50" name="seznam_sestavin" class="mb-1">vsako sestavino podaj v svoji vrstici</textarea><br>
    Čas priprave: <input type="text" name="cas_priprave"  class="mb-1"><br>
    Kolorijska vrednost: <input type="text" name="kalorijska_vrednost" class="mb-1"><br>
    Navodila: <textarea rows="10" cols="50" name="navodila" class="mb-1"></textarea><br>
    <input type="submit" value="Dodaj">
</form>

 