---
title: |
       | **COL703 - Assignment 1**
author:
  - name: Ramneet Singh
    affiliation: 2019CS50445
date: September 2022
# abstract:
# keywords:
# thanks:

## Formatting
fontsize: 12pt
# mainfont: "gentium" # See https://fonts.google.com/ for fonts
# sansfont: "Raleway"
# monofont: "IBM Plex Mono"
mathfont: ccmath
# fontfamily: concrete | gentium | libertine
# documentclass: article | scrartcl
# fontfamily: concrete
titlepage: true
colorlinks: true
toc: true
# numbersections: true
secnumdepth: 3
block-headings: true

output: 
  pdf_document:
    pandoc_args: "--highlight=breezedark"

documentclass: article
classoption:
 - oneside
# fontenc: T1
geometry:
 - a4paper
 - heightrounded
header-includes:
 - |
  ```{=latex}
  \usepackage{amsmath,amsfonts,fancyhdr,float,array,ebproof,logicproof,amsthm}
  \floatplacement{figure}{H}
  \usepackage{listings}
  \lstset{basicstyle=\ttfamily,
    showstringspaces=false,
    commentstyle=\color{red},
    keywordstyle=\color{blue}
  }
  \newcounter{proofrow}
  \newenvironment{prooftabular}{%
  \let\oldarraystretch\arraystretch
  \renewcommand{\arraystretch}{1.5}
  \begin{tabular}{%
      @{\stepcounter{proofrow}\theproofrow}%
      p{1em}@{}>{\(}l<{\)}>{\quad}l%
  }
  }{%
  \end{tabular}
  \renewcommand{\arraystretch}{\oldarraystretch}  }
  \newcommand{\hlineproofbox}{\cline{2-2}}
  \newcommand{\proofboxed}[1]{\multicolumn{1}{|>{\(}l<{\)}@{\ }|}{#1}}
  \newtheorem{theorem}{Theorem}
  ```
pagestyle: headings
---

**Note:** The Modus Ponens proof rule we will use in this assignment is
$$
\begin{prooftree}
    \hypo{\phi} \hypo{\phi \rightarrow \psi}
    \infer2[($\rightarrow$e or MP)]{\psi}
\end{prooftree}
$$ 

\newpage

# Question 1

<!-- ## Part (a) -->

<!-- The sequent is valid. **To Show:** $\neg p \rightarrow \neg q \vdash q \rightarrow p$. -->

<!-- \begin{logicproof}{2} -->
<!--     \neg p \rightarrow \neg q & premise \\ -->
<!--     \begin{subproof} -->
<!--         q                     & assumption \\ -->
<!--         \begin{subproof} -->
<!--             \neg p            & assumption \\ -->
<!--             \neg q            & $\rightarrow$e 3,1 \\ -->
<!--             \perp             & $\neg$e 2,4 -->
<!--         \end{subproof} -->
<!--         \neg \neg p           & $\neg$i 3-5 \\ -->
<!--         p                     & $\neg \neg$e 6 -->
<!--     \end{subproof} -->
<!--     q \rightarrow p           & $\rightarrow$i 2-7 -->
<!-- \end{logicproof} -->

## Part (b)

The sequent is valid. **To Show:** $\neg p, p \lor q \vdash q$.

\begin{logicproof}{1}
    \neg p                  & premise \\
    p \lor q                & premise \\
    \begin{subproof}
        p              & assumption \\
        \perp          & $\neg$e 3,1 \\
        q              & $\perp$e 4
    \end{subproof}
    \begin{subproof}
        q              & assumption \\
        q              & copy 6
    \end{subproof}
    q                  & $\lor$e 2,3-5,6-7
\end{logicproof}

## Part (d)

The sequent is valid. **To Show:** $p \land \neg p \vdash \neg(r \rightarrow q) \land (r \rightarrow q)$.

\begin{logicproof}{1}
    p \land \neg p          & premise \\
    p                       & $\land$e$_1$ 1 \\
    \neg p                  & $\land$e$_2$ 1 \\
    \perp                   & $\neg$e 2,3 \\
    \neg(r \rightarrow q) \land (r \rightarrow q) & $\perp$e 4
\end{logicproof}

\newpage

# Question 3

We design the following introduction and elimination rules for $\leftrightarrow$:
$$
    \begin{prooftree}
        \hypo{\phi \rightarrow \psi} \hypo{\psi \rightarrow \phi}
        \infer2[($\leftrightarrow$i)]{\phi \leftrightarrow \psi}
    \end{prooftree}
$$ 
$$
    \begin{prooftree}
        \hypo{\phi \leftrightarrow \psi} \hypo{\phi}
        \infer2[($\leftrightarrow$e$_1$)]{\psi}
    \end{prooftree}
    \qquad
    \begin{prooftree}
        \hypo{\phi \leftrightarrow \psi} \hypo{\psi}
        \infer2[($\leftrightarrow$e$_2$)]{\phi}
    \end{prooftree}
$$

We also have the following two rules similar to Modus Tollens in Natural Deduction:
$$
    \begin{prooftree}
        \hypo{\phi \leftrightarrow \psi} \hypo{\neg \phi}
        \infer2[($\leftrightarrow$MT$_1$)]{\neg \psi}
    \end{prooftree}
    \qquad
    \begin{prooftree}
        \hypo{\phi \leftrightarrow \psi} \hypo{\neg \psi}
        \infer2[($\leftrightarrow$MT$_2$)]{\neg \phi}
    \end{prooftree}
$$

We will show that each of these can be derived using the existing natural deduction rules if we replace $\phi \leftrightarrow \psi$ with $(\phi \rightarrow \psi) \land (\psi \rightarrow \phi)$.

$\boldsymbol{\leftrightarrow}$**i**: We will show that $\phi \rightarrow \psi, \psi \rightarrow \phi \vdash (\phi \rightarrow \psi) \land (\psi \rightarrow \phi)$.
\begin{logicproof}{0}
    \phi \rightarrow \psi & premise \\
    \psi \rightarrow \phi & premise \\
    (\phi \rightarrow \psi) \land (\psi \rightarrow \phi) & $\land$i 1,2
\end{logicproof}

$\boldsymbol{\leftrightarrow}$**e**$\boldsymbol{_1}$: We will show that $(\phi \rightarrow \psi) \land (\psi \rightarrow \phi), \phi \vdash \psi$.
\begin{logicproof}{0}
    (\phi \rightarrow \psi) \land (\psi \rightarrow \phi) & premise \\
    \phi                                                  & premise \\
    \phi \rightarrow \psi                                 & $\land$e$_1$ 1 \\
    \psi                                                  & $\rightarrow$e 2,3
\end{logicproof}

$\boldsymbol{\leftrightarrow}$**e**$\boldsymbol{_2}$: We will show that $(\phi \rightarrow \psi) \land (\psi \rightarrow \phi), \psi \vdash \phi$.
\begin{logicproof}{0}
    (\phi \rightarrow \psi) \land (\psi \rightarrow \phi) & premise \\
    \psi                                                  & premise \\
    \psi \rightarrow \phi                                 & $\land$e$_2$ 1 \\
    \phi                                                  & $\rightarrow$e 2,3
\end{logicproof}

$\boldsymbol{\leftrightarrow}$**MT**$\boldsymbol{_1}$: We will show that $(\phi \rightarrow \psi) \land (\psi \rightarrow \phi), \neg \phi \vdash \neg \psi$.
\begin{logicproof}{1}
    (\phi \rightarrow \psi) \land (\psi \rightarrow \phi) & premise \\
    \neg \phi                                             & premise \\
    \begin{subproof}
        \psi                                              & assumption \\
        \psi \rightarrow \phi                             & $\land$e$_2$ 1 \\
        \phi                                              & $\rightarrow$e 3,4 \\
        \perp                                             & $\neg$e 5,2
    \end{subproof}
    \neg \psi                                             & $\neg$i 3-6
\end{logicproof}

$\boldsymbol{\leftrightarrow}$**MT**$\boldsymbol{_2}$: We will show that $(\phi \rightarrow \psi) \land (\psi \rightarrow \phi), \neg \psi \vdash \neg \phi$.
\begin{logicproof}{1}
    (\phi \rightarrow \psi) \land (\psi \rightarrow \phi) & premise \\
    \neg \psi                                             & premise \\
    \begin{subproof}
        \phi                                              & assumption \\
        \phi \rightarrow \psi                             & $\land$e$_1$ 1 \\
        \psi                                              & $\rightarrow$e 3,4 \\
        \perp                                             & $\neg$e 5,2
    \end{subproof}
    \neg \phi                                             & $\neg$i 3-6
\end{logicproof}

\newpage

# Question 4

## Part (c)

**To Show:** $(p \rightarrow r) \land (q \rightarrow r) \vdash p \land q \rightarrow r$.

\begin{logicproof}{1}
    (p \rightarrow r) \land (q \rightarrow r) & premise \\
    \begin{subproof}
        p \land q                             & assumption \\
        p                                     & $\land$e$_1$ 2 \\
        p \rightarrow r                       & $\land$e$_1$ 1 \\
        r                                     & $\rightarrow$e 3,4
    \end{subproof}
    p \land q \rightarrow r                   & $\rightarrow$i 2-5
\end{logicproof}

## Part (d)

**To Show:** $p \rightarrow q \land r \vdash (p \rightarrow q) \land (p \rightarrow r)$.

\begin{logicproof}{1}
    p \rightarrow q \land r                   & premise \\
    \begin{subproof}
        p                                     & assumption \\
        q \land r                             & $\rightarrow$e 2,1 \\
        q                                     & $\land$e$_1$ 3
    \end{subproof}
    p \rightarrow q                           & $\rightarrow$i 2-4 \\
    \begin{subproof}
        p                                     & assumption \\
        q \land r                             & $\rightarrow$e 6,1 \\
        r                                     & $\land$e$_2$ 7
    \end{subproof}
    p \rightarrow r                           & $\rightarrow$i 6-8 \\
    (p \rightarrow q) \land (p \rightarrow r) & $\land$i 5,9
\end{logicproof}

\newpage

# Question 7

No, $\{\leftrightarrow, \neg\}$ is not an adequate set of connectives. A counter-example is the formula $p \lor q$ (where $p,q$ are propositional atoms), for which there is no equivalent formula formed only from the connectives $\{\leftrightarrow, \neg\}$. Formally, we prove this using the following theorem:

\begin{theorem}
    Let $\phi$ be any formula formed using the connectives $\{\leftrightarrow,\neg\}$ and containing at least $2$ propositional atoms. Then, any sub-formula of $\phi$ evaluates to $\tt{T}$ in an even number of lines in the truth table of $\phi$.
\end{theorem}
\begin{proof}
    Let $\psi$ be a sub-formula of $\phi$. The proof is by structural induction on $\psi$. Before beginning, note that since $\phi$ has at least $2$ propositional atoms, the number of lines in its truth table is a multiple of $4$.

    \textbf{Base Case:} $\psi = p$ (A propositional atom). By definition of a truth table, $p$ is \texttt{T} in half the lines in the truth table and \texttt{F} in the rest. Since the number of lines is a multiple of $4$, $\psi$ is \texttt{T} in an even number of lines.

    \textbf{Induction Step:} We consider the following two cases:
    \begin{itemize}
        \item $\psi = \neg \psi_1$. Now, $\psi_1$ is also a sub-formula of $\phi$, and by the Induction Hypothesis evaluates to \texttt{T} in an even number of lines (call it $n_1$). If the total number of lines in the truth table is $n$, this means it evaluates to \texttt{F} in $n-n_1$ lines. Since $\psi=\neg \psi_1$, by definition of $\neg$, it evaluates to \texttt{T} in exactly those lines in which $\psi_1$ evaluates to \texttt{F}, implying that it is \texttt{T} in $n-n_1$ lines. Now, $n \operatorname{mod} 4 = 0$ and $n_1 \operatorname{mod} 2 = 0$, therefore $(n-n_1) \operatorname{mod} 2 = 0$, meaning $\psi$ is \texttt{T} in an even number of lines.
        \item $\psi = \psi_1 \leftrightarrow \psi_2$. Now, $\psi_1$ and $\psi_2$ are also sub-formulae of $\phi$, and by the Induction Hypothesis evaluate to \texttt{T} in an even number of lines in the truth table. Let $n$ be the total number of lines in the truth table. Suppose $\psi_1$ is \texttt{T} in $n_1$ lines, of which $\psi_2$ is true in $m_1$ of them. Among the $n-n_1$ lines in which $\psi_1$ is \texttt{F}, suppose $\psi_2$ is \texttt{T} in $m_2$ of them. By definition of $\leftrightarrow$, $\psi$ is \texttt{T} whenever $\psi_1$ and $\psi_2$ have the same truth value. So the number of lines in which $\psi$ is \texttt{T} is $m_1 + (n - n_1 - m_2)$, call this $k$. Note that the number of lines in which $\psi_2$ is \texttt{T} is $m_1+m_2$, which we know to be even (from I.H.). It follows that $m_1 \operatorname{mod} 2 = m_2 \operatorname{mod} 2$, which implies that $(m_1-m_2) \operatorname{mod} 2 = 0$. This implies that $k \operatorname{mod} 2 = (n-n_1) \operatorname{mod} 2$ since $k = m_1-m_2+n-n_1$. Finally, note that $n \operatorname{mod} 4 = 0$ and $n_1 \operatorname{mod} 2 = 0$, therefore $(n-n_1) \operatorname{mod} 2 = 0$, meaning $k$ is even, i.e., $\psi$ is \texttt{T} in an even number of lines.
    \end{itemize}
\end{proof}

We can use the theorem above to show that $p \lor q$ cannot have an equivalent formula formed using the connectives $\{\leftrightarrow,\neg\}$. The proof is by contradiction. Suppose there is such an equivalent formula $\phi$. Since equivalent formulae must have the same truth table, we know that $\phi$ evaluates to \texttt{T} for exactly the same valuations of $p,q$ under which $p \lor q$ evaluates to \texttt{T}. From the truth table of $p \lor q$ (see the figure below), we know it evaluates to \texttt{T} in an odd number of lines. But, since every formula is a sub-formula of itself (and also because $\phi$ is formed from $\{\leftrightarrow,\neg\}$ and has at least two atoms $p,q$), we can apply the above theorem to $\phi$ to conclude that it evaluates to \texttt{T} in an even number of lines. This is a contradiction, and therefore, no such equivalent formula exists. This proves that $\{\leftrightarrow,\neg\}$ is not an adequate set of connectives for propositional logic.

\begin{displaymath}
\begin{array}{|c c|c|}
% |c c|c| means that there are three columns in the table and
% a vertical bar ’|’ will be printed on the left and right borders,
% and between the second and the third columns.
% The letter ’c’ means the value will be centered within the column,
% letter ’l’, left-aligned, and ’r’, right-aligned.
p & q & p \lor q\\ % Use & to separate the columns
\hline % Put a horizontal line between the table header and the rest.
T & T & T\\
T & F & T\\
F & T & T\\
F & F & F\\
\end{array}
\end{displaymath}

\newpage

# Question 8

## Part (b)

Choose the valuation $v$ such that $v(p) = \texttt{T}, v(q) = \texttt{F}, v(r) = \tt{T}$. Then, $v(\neg r) = \tt{F}$, which implies that $v(\neg r \rightarrow (p \lor q)) = \tt{T}$. Further, since $v(r) = \tt{T}$ and $v(\neg q) = \tt{T}$, we have $v(r \land \neg q) = \tt{T}$. So both the formulae to the left of the $\vdash$ evaluate to \texttt{T}. The formula to the right is $r \rightarrow q$. Since $v(r) = \tt{T}$ and $v(q) = \tt{F}$, we get $v(r \rightarrow q) = \tt{F}$. So the formula to the right of the $\vdash$ evaluates to \texttt{F}. The existence of such a valuation implies that the sequent $\neg r \rightarrow (p \lor q), r \land \neg q \vdash r \rightarrow q$ is not valid.

## Part (d)

Choose the valuation $v$ such that $v(p) = \texttt{T}, v(q) = \texttt{F}, v(r) = \texttt{T}$. Then, since $v(q) = \tt{F}$, we get $v(q \rightarrow r) = \tt{T}$. Since $v(p) = \tt{T}$ and $v(q \rightarrow r) = \tt{T}$, we get $v(p \rightarrow (q \rightarrow r)) = \tt{T}$. So the formula to the left of the $\vdash$ evaluates to \texttt{T}. The formula to the right is $p \rightarrow (r \rightarrow q)$. Since $v(r) = \tt{T}$ and $v(q) = \tt{F}$, we get $v(r \rightarrow q) = \tt{F}$. Since $v(p) = \tt{T}$ and $v(r \rightarrow q) = \tt{F}$, we can conclude $v(p \rightarrow (r \rightarrow q)) = \tt{F}$. So the formula to the right of the $\vdash$ evaluates to \texttt{F}. The existence of such a valuation implies that the sequent $p \rightarrow (q \rightarrow r) \vdash p \rightarrow (r \rightarrow q)$ is not valid.
