%rebase('bootstrap.tpl')
    % if 3 > 5:
    % c = 5
    % else:
    % c = 100
    % end
    % print('tole gre v terminal')
        <em>Živjo</em> ,  <b>{{ime}}</b>! A veš, da je a enako {{ c }}?
        % if ime == 'Ana':
        Zate imam nekaj posebnega! Kvadrat števil od 0 do 4:
        <ul>
            % for i in range(5):
            <li>{{ i ** 2  }}</li>
            %end
        </ul>
        % else:
        Zate {{ ime }} mi je popolnoma vseeno.
        %end

        <form action='/sestej/'>
            <h2>sestevanje</h2>
            a: <input type='text' name='a' value="20">
            b: <input type='text' name='b' placeholder="30">
            <input type='submit' value='a + b'>
        </form>

