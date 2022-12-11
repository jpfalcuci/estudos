<?php

    // $ php -a (interactive shell)

    $regexp = '~(\d\d)(\w)~';
    $alvo = '12a34b56c';
    
    $achou = preg_match($regexp, $alvo, $match);
    echo $achou;    // 1
    print_r($match);
    /* Array
    (
        [0] => 12a
        [1] => 12
        [2] => a
    ) */
    echo $match[0]; // 12a
    
    $achou = preg_match_all($regexp, $alvo, $match);
    echo $achou;    // 3
    print_r($match);
    /* Array
    (
        [0] => Array
            (
                [0] => 12a
                [1] => 34b
                [2] => 56c
            )

        [1] => Array
            (
                [0] => 12
                [1] => 34
                [2] => 56
            )

        [2] => Array
            (
                [0] => a
                [1] => b
                [2] => c
            )

    ) */

    $achou = preg_match($regexp, $alvo, $match, PREG_OFFSET_CAPTURE);
    echo $achou;    // 1
    print_r($match);
    /* Array
    (
        [0] => Array
            (
                [0] => 12a
                [1] => 0
            )

        [1] => Array
            (
                [0] => 12
                [1] => 0
            )

        [2] => Array
            (
                [0] => a
                [1] => 2
            )

    ) */

?>