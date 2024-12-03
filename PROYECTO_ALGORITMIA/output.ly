\version "2.24.0"
\header {
    title = "Su cancioncita xd"
    composer = "creado por su chill de cojones"
}

\paper {
    #(set-paper-size "a4")
    top-margin = 15
    left-margin = 15
    right-margin = 10
    bottom-margin = 15
}

\score {
    \relative c' {
        \tempo 4 = 120
        \time 4/4
        \clef treble
        \key c \major
        
        c4  c4  g4  g4  a4  a4  g4  f4  f4  e4  e4  d4  d4  c4 
        \bar "|."
    }
    \layout { 
        indent = #0
    }
    \midi { }
}