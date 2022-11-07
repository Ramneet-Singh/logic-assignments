---
title: "**COL703 - Assignment 4**"
author:
  - name: "Ramneet Singh"
    affiliation: "2019CS50445"
date: November 2022
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
numbersections: false
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
  \usepackage{amsmath,amsfonts,amsthm,fancyhdr,float,fullpage,mathtools,logicproof}
  \floatplacement{figure}{H}
  \usepackage{listings}
  \lstset{basicstyle=\ttfamily,
    showstringspaces=false,
    commentstyle=\color{red},
    keywordstyle=\color{blue}
  }
  \newtheorem{theorem}{Theorem}
  \newtheorem{corollary}{Corollary}[section]
  \newtheorem{lemma}{Lemma}
  \theoremstyle{definition}
  \newtheorem{remark}{Remark}
  \newtheorem{definition}{Definition}
  \newcommand\satisfies{\vDash}
  \newcommand\entails{\vDash}
  \newcommand\derives{\vdash}
  \newcommand\arrow{\rightarrow}
  \newcommand*{\defeq}{\stackrel{\text{def}}{=}}
  \newcommand\numberthis{\addtocounter{equation}{1}\tag{\theequation}}
  ```
pagestyle: headings
---

\newpage

# Question 1

We have the following three first-order logic formulas representing points (a), (b) and (c) given in the question:
\begin{align*}
    F_1 &:\quad \forall x ( B(x) \arrow \forall y ( \neg S(y,y) \arrow S(x,y) ) ) \\
    F_2 &:\quad \neg \exists x \exists y ( B(x) \land S(x,y) \land S(y,y) ) \\
    F_3 &:\quad \neg (\exists x B(x))
\end{align*}

To show $F_1 \land F_2 \entails F_3$, we will show that the formula $F_1 \land F_2 \land \neg F_3$ is unsatisfiable. First, we Skolemise each of the conjuncts and convert their matrices into CNF to get the following three formulas:
\begin{align*}
    G_1 &:\quad \forall x \forall y (\quad \neg B(x) \lor S(y,y) \lor S(x,y) \quad) \\
    G_2 &:\quad \forall x \forall y (\quad \neg B(x) \lor \neg S(x,y) \lor \neg S(y,y) \quad) \\
    G_3 &:\quad B(c)
\end{align*} where $c$ is a fresh constant symbol.

The formula $F_1 \land F_2 \land \neg F_3$ is equisatisfiable with $G_1 \land G_2 \land G_3$. Thus it suffices to give a ground resolution refutation of $G_1 \land G_2 \land G_3$. Now we derive $\Box$ from ground instances of clauses in the respective matrices of the formulas $G_1,G_2,G_3$.

\begin{logicproof}{0}
    \{ \neg B(c), S(c,c) \} & clause of $G_1$'s matrix with $[c/x][c/y]$ \\
    \{ \neg B(c), \neg S(c,c) \} & clause of $G_2$'s matrix with $[c/x][c/y]$ \\
    \{ \neg B(c) \} & 1,2 resolution \\
    \{ B(c) \} & clause of $G_3$'s matrix \\
    \Box & 3,4 resolution
\end{logicproof}

By the ground resolution theorem, $G_1 \land G_2 \land G_3$ is unsatisfiable, which implies that $F_1 \land \land F_2 \land \neg F_3$ is unsatisfiable. Therefore, we can conclude that $F_1 \land F_2 \entails F_3$.

\newpage

# Question 2

Let $\sigma$ be a signature and $\sim$ be a relation on $\sigma$-assignments which satisfies the following properties:

1. If $\mathcal{A} \sim \mathcal{B}$, then for every atomic formula $F$ we have $\mathcal{A} \satisfies F$ iff $\mathcal{B} \satisfies F$.
2. If $\mathcal{A} \sim \mathcal{B}$, then for each variable $x$ we have:
    A.  For each $a \in U_{\mathcal{A}}$, there exists $b \in U_{\mathcal{B}}$ such that $A_{[x \;\mapsto\; a]} \sim B_{[x \;\mapsto\; b]}$.
    B.  For each $b \in U_{\mathcal{B}}$, there exists $a \in U_{\mathcal{A}}$ such that $\mathcal{A}_{[x \;\mapsto\; a]} \sim \mathcal{B}_{[x \;\mapsto\; b]}$.

We have the following theorem.

\begin{theorem}
    If $\mathcal{A} \sim \mathcal{B}$, then for every formula $F$ we have $\mathcal{A} \satisfies F$ iff $\mathcal{B} \satisfies F$.
\end{theorem}
\begin{proof}
    Suppose $\mathcal{A} \sim \mathcal{B}$. We will show by induction on the structure of $F$ that for every formula $F$, $\mathcal{A} \satisfies F$ iff $\mathcal{B} \satisfies F$.

    \begin{itemize}
        \item \textbf{Base Case:} $F$ is an atomic formula. From property 1, we have $\mathcal{A} \satisfies F$ iff $\mathcal{B} \satisfies F$.
        \item \textbf{Induction Step:} We consider the following three cases:
        \begin{itemize}
            \item $F = F_1 \land F_2$. We have:
                \begin{alignat*}{2}
                              &\; \mathcal{A} \satisfies F && \\
                    \text{iff}&\; \mathcal{A} \satisfies F_1 \land F_2 && \\
                    \text{iff}&\; \mathcal{A} \satisfies F_1 \text{ and } \mathcal{A} \satisfies F_2 &&\; \text{(defn. of } \satisfies \text{)} \\
                    \text{iff}&\; \mathcal{B} \satisfies F_1 \text{ and } \mathcal{B} \satisfies F_2 &&\; \text{(induction hypothesis)} \\
                    \text{iff}&\; \mathcal{B} \satisfies F_1 \land F_2 &&\; \text{(defn. of } \satisfies \text{)} \\
                    \text{iff}&\; \mathcal{B} \satisfies F &&
                \end{alignat*}
            \item $F = \neg F_1$. We have:
                \begin{alignat*}{2}
                              &\; \mathcal{A} \satisfies F && \\
                    \text{iff}&\; \mathcal{A} \satisfies \neg F_1 && \\
                    \text{iff}&\; \mathcal{A} \not\satisfies F_1 &&\; \text{(defn. of } \satisfies \text{)} \\
                    \text{iff}&\; \mathcal{B} \not\satisfies F_1 &&\; \text{(induction hypothesis)} \\
                    \text{iff}&\; \mathcal{B} \satisfies \neg F_1 &&\; \text{(defn. of } \satisfies \text{)} \\
                    \text{iff}&\; \mathcal{B} \satisfies F
                \end{alignat*}
            \item $F = \exists x F_1$. In this case, we show that $\mathcal{A} \satisfies F$ iff $\mathcal{B} \satisfies F$ by showing both the directions separately.
                \begin{itemize}
                    \item \emph{(only if):} Suppose $\mathcal{A} \satisfies F$. By definition of $\satisfies$, there exists $a \in U_{\mathcal{A}}$ such that $\mathcal{A}_{[x \;\mapsto\; a]} \satisfies F_1$. From Property 2A, we know that there exists $b \in U_{\mathcal{B}}$ such that $\mathcal{A}_{[x \;\mapsto\; a]} \sim \mathcal{B}_{[x \;\mapsto\; b]}$. Given this, we can apply the induction hypothesis on $F_1$ to conclude, from $\mathcal{A}_{[x \;\mapsto\; a]} \satisfies F_1$, that $\mathcal{B}_{[x \;\mapsto\; b]} \satisfies F_1$. From the definition of $\satisfies$, this implies that $\mathcal{B} \satisfies \exists x F_1$. Thus $\mathcal{B} \satisfies F$.
                    \item \emph{(if):} Suppose $\mathcal{B} \satisfies F$. By definition of $\satisfies$, there exists $b \in U_{\mathcal{B}}$ such that $\mathcal{B}_{[x \;\mapsto\; b]} \satisfies F_1$. From Property 2B, we know that there exists $a \in U_{\mathcal{A}}$ such that $\mathcal{A}_{[x \;\mapsto\; a]} \sim \mathcal{B}_{[x \;\mapsto\; b]}$. Given this, we can apply the induction hypothesis on $F_1$ to conclude, from $\mathcal{B}_{[x \;\mapsto\; b]} \satisfies F_1$, that $\mathcal{A}_{[x \;\mapsto\; a]} \satisfies F_1$. From the definition of $\satisfies$, this implies that $\mathcal{A} \satisfies \exists x F_1$. Thus $\mathcal{A} \satisfies F$.
                \end{itemize}
        \end{itemize}
        Since we have shown $\mathcal{A} \satisfies F$ iff $\mathcal{B} \satisfies F$ in all the three cases and they are exhaustive, the induction step is complete.
    \end{itemize}

    From the principle of structural induction, we can conclude that for every formula $F$, $\mathcal{A} \satisfies F$ iff $\mathcal{B} \satisfies F$.
\end{proof}

\newpage

# Question 3

We have the following four first-order logic formulas representing points (a), (b), (c) and (d) given in the question:
\begin{align*}
    F_1 &:\quad \forall x (\; (\forall y (\; C(x,y) \arrow R(y) \;)) \arrow H(x) \;) \\
    F_2 &:\quad \forall x (\; G(x) \arrow R(x) \;) \\
    F_3 &:\quad \forall x (\; (\exists y (\; G(y) \land C(y,x) \;)) \arrow G(x) \;) \\
    F_4 &:\quad \forall x (\; G(x) \arrow H(x) \;)
\end{align*}

To show $F_1 \land F_2 \land F_3 \entails F_4$, we will show that $F_1 \land F_2 \land F_3 \land \neg F_4$ is unsatisfiable. Skolemising each of the conjuncts and converting their matrices to CNF, we get the following formulas.
\begin{align*}
    G_1 &:\quad \forall x (\; (C(x,f(x)) \lor H(x)) \;\land\; (\neg R(f(x)) \lor H(x)) \;) \\
    G_2 &:\quad \forall x (\; \neg G(x) \lor R(x) \;) \\
    G_3 &:\quad \forall x \forall y(\; \neg G(y) \lor \neg C(y,x) \lor G(x) \;) \\
    G_4 &:\quad G(c) \;\land\; \neg H(c)
\end{align*} where $f$ is a fresh function symbol and $c$ is a fresh constant symbol.

The formula $G_1 \land G_2 \land G_3 \land G_4$ is equisatisfiable with $F_1 \land F_2 \land F_3 \land \neg F_4$. Thus it suffices to show a predicate logic resolution refutation of $G_1 \land G_2 \land G_3 \land G_4$. The proof is as follows. Note that we subscript the variables in line $k$ with $k$ to ensure we always resolve clauses with disjoint sets of variables.
\begin{logicproof}{0}
    \{\, G(c) \,\} & clause of $G_4$ \\
    \{\, \neg G(y_2), \neg C(y_2,x_2), G(x_2) \,\} & clause of $G_3$ \\
    \{\, \neg C(c,x_3), G(x_3) \,\} & 1,2 Res. $D_1=\{G(c)\}, D_2=\{\neg G(y_2)\}, \theta=[c/y_2].[x_3/x_2]$ \\
    \{\, \neg G(x_4), R(x_4) \,\} & clause of $G_2$ \\
    \{\, \neg C(c,x_5), R(x_5) \,\} & 3,4 Res. $D_1=\{G(x_3)\}, D_2=\{\neg G(x_4)\}, \theta=[x_3/x_4].[x_5/x_3]$ \\
    \{\, C(x_6,f(x_6)), H(x_6) \,\} & clause of $G_1$ \\
    \{\, R(f(c)), H(c) \,\} & 6,5 Res $D_1=\{C(x_6,f(x_6))\} D_2=\{\neg C(c,x_5)\} \theta=[c/x_6].[f(c)/x_5]$ \\
    \{\, \neg R(f(x_8)), H(x_8) \,\} & clause of $G_1$ \\
    \{\, H(c) \,\} & 7,8 Res. $D_1=\{R(f(c))\}, D_2=\{\neg R(f(x_8))\}, \theta=[c/x_8]$ \\
    \{\, \neg H(c) \,\} & clause of $G_1$ \\
    \Box & 9,10 Res. $D_1=\{H(c)\}, D_2=\{\neg H(c)\}, \theta=\text{Identity}$
\end{logicproof}

Therefore, $G_1 \land G_2 \land G_3 \land G_4$ is unsatisfiable, which implies that $F_1 \land F_2 \land F_3 \land \neg F_4$ is unsatisfiable. Then we can conclude that $F_1 \land F_2 \land F_3 \entails F_4$.

\newpage

# Question 4

Let $A(x_1, \dots, x_n)$ be a formula with no quantifiers and no function symbols. We have the following theorem.

\begin{theorem}
    The formula $F = \forall x_1 \dots \forall x_n A(x_1, \dots, x_n)$ is satisfiable if and only if it is satisfiable in an interpretation with just one element in the universe.
\end{theorem}
\begin{proof}
    \textbf{(If):} If there is a model $\mathcal{A}$ such that $|U_{\mathcal{A}}| = 1$ and $\mathcal{A} \satisfies F$, then $F$ is satisfiable since there exists a satisfying model.

    \textbf{(Only If):} Assume that $F$ is satisfiable. Let $\mathcal{A}$ be a model that satisfies $F$. By definition of satisfaction, we have
    $$
    \mathcal{A}_{[x_1 \;\mapsto\; a_1][x_2 \;\mapsto\; a_2]\dots[x_n \;\mapsto\; a_n]} \satisfies A(x_1,\dots,x_n) \text{ for all } a_1,a_2,\dots,a_n \in U_{\mathcal{A}}
    $$ Pick any $a \in U_{\mathcal{A}}$. In particular, we have
    \begin{equation}
        \label{eq:1}
        \mathcal{A}_{[x_1 \;\mapsto\; a][x_2 \;\mapsto\; a]\dots[x_n \;\mapsto\; a]} \satisfies A(x_1,\dots,x_n)
    \end{equation}

    We now define a new model $\mathcal{B}$ as follows (note that there are no constants or function symbols in the signature):
    \begin{itemize}
        \item $U_{\mathcal{B}} = \{ a \}$.
        \item For each $k$-ary predicate symbol $P$ in $A(x_1,\dots,x_n)$, $(a,\dots,a) \in P_{\mathcal{B}}$ iff $(a,\dots,a) \in P_{\mathcal{A}}$.
    \end{itemize}

    \textbf{Claim:} $\mathcal{B}_{[x_1 \;\mapsto\; a][x_2 \;\mapsto\; a]\dots[x_n \;\mapsto\; a]} \satisfies A(x_1,\dots,x_n)$.
    
    \textbf{Proof:} Consider any atomic formula in $A(x_1,\dots,x_n)$. Since there are no function symbols, it must be of the form $P(x_{i_1}, \dots, x_{i_k})$ where $i_1,\dots,i_k \in \{1,\dots,n\}$. We have
        \begin{alignat*}{2}
                      &\; \mathcal{B}_{[x_1 \;\mapsto\; a][x_2 \;\mapsto\; a]\dots[x_n \;\mapsto\; a]} \satisfies P(x_{i_1}, \dots, x_{i_k}) && \\
            \text{iff}&\; (a,\dots,a) \in P_{\mathcal{B}} &&\; \text{(defn. of } \satisfies \text{)} \\
            \text{iff}&\; (a,\dots,a) \in P_{\mathcal{A}} &&\; \text{(defn. of } \mathcal{B} \text{)} \\
            \text{iff}&\; \mathcal{A}_{[x_1 \;\mapsto\; a][x_2 \;\mapsto\; a]\dots[x_n \;\mapsto\; a]} \satisfies P(x_{i_1}, \dots, x_{i_k}) &&\; \text{(defn. of } \satisfies \text{)}
        \end{alignat*}
    So the models $\mathcal{B}_{[x_1 \;\mapsto\; a][x_2 \;\mapsto\; a]\dots[x_n \;\mapsto\; a]}$ and $\mathcal{A}_{[x_1 \;\mapsto\; a][x_2 \;\mapsto\; a]\dots[x_n \;\mapsto\; a]}$ assign the same truth value to each atomic formula occurring in $A(x_1,\dots,x_n)$. Since $A(x_1,\dots,x_n)$ is formed from atomic formulas using propositional connectives (no quantifiers), this implies that they both assign the same truth value to $A(x_1,\dots,x_n)$. From equation \ref{eq:1}, we know that $\mathcal{A}_{[x_1 \;\mapsto\; a][x_2 \;\mapsto\; a]\dots[x_n \;\mapsto\; a]} \satisfies A(x_1,\dots,x_n)$. Thus we get that
    $$
    \mathcal{B}_{[x_1 \;\mapsto\; a][x_2 \;\mapsto\; a]\dots[x_n \;\mapsto\; a]} \satisfies A(x_1,\dots,x_n)
    $$
    This completes the proof of the claim. Since $a$ is the only element in $U_{\mathcal{B}}$, we further get
    $$
    \mathcal{B}_{[x_1 \;\mapsto\; a_1][x_2 \;\mapsto\; a_2]\dots[x_n \;\mapsto\; a_n]} \satisfies A(x_1,\dots,x_n) \text{ for all } a_1,a_2,\dots,a_n \in U_{\mathcal{B}}
    $$ From the definition of satisfaction, we get
    $$
    \mathcal{B} \satisfies \forall x_1 \dots \forall x_n A(x_1,\dots,x_n)
    $$ Thus $\mathcal{B}$ is a model that satisfies $F$ and has only one element in the universe. We started with a model $\mathcal{A}$ that satisfies $F$ and constructed a model with only one element in the universe which satisfies $F$. Therefore, $F$ is satisfiable \textbf{only if} it is satisfiable in a model with just one element in the universe.
\end{proof}

\newpage

# Question 5

## Part (a)

Let $\sigma$ be a signature with only one binary relation symbol $R$. Let $n$ be a positive integer. Define the formula $F_n$ as follows:
\begin{align*}
F_n \defeq& (\; \forall x (\; \neg R(x,x) \;) \\
          &\land\; \forall x \forall y \forall z (\; (R(x,y) \land R(y,z)) \arrow R(x,z) \;) \\
          &\land\; \exists x_1 \exists x_2 \dots \exists x_n (\; R(x_1,x_2) \land R(x_2,x_3) \land \dots \land R(x_{n-1},x_n) \;))
\end{align*}

We have the following theorem.
\begin{theorem}
    Every model $\mathcal{A}$ which satisfies $F_n$ has at least $n$ elements.
\end{theorem}
\begin{proof}
    The proof is by contradiction. Assume, if possible, that there is a model $\mathcal{A}$ such that $\mathcal{A} \satisfies F_n$ and $|U_{\mathcal{A}}| < n$. Since $\mathcal{A}$ satisfies the third conjunct of $F_n$, we know there exist $a_1,\dots,a_n \in U_{\mathcal{A}}$ such that 
$$
    \mathcal{A}_{[x_1 \;\mapsto\; a_1]\dots[x_n \;\mapsto\; a_n]} \satisfies (R(x_1,x_2) \land \dots \land R(x_{n-1},x_n))
$$ 
    This is true if and only if we have $(a_1,a_2), (a_2,a_3), \dots, (a_{n-1},a_n) \in R_{\mathcal{A}}$. Now, we claim that for any $i,j \in \{1,\dots,n\}$ with $i \neq j$, we have $a_i \neq a_j$.

    \emph{Proof:} W.l.o.g, assume $i<j$. We know from above that $(a_i,a_{i+1}), (a_{i+1},a_{i+2}), \dots, (a_{j-1},a_j) \in R_{\mathcal{A}}$. Since $\mathcal{A}$ satisfies the second conjunct of $F_n$, we have for all $a,b,c \in U_{\mathcal{A}}$, if $(a,b), (b,c) \in R_{\mathcal{A}}$, then $(a,c) \in R_{\mathcal{A}}$. We can apply this to the chain from $a_i$ to $a_j$ ($j-i-1$ times) to get $(a_i,a_j) \in R_{\mathcal{A}}$. Finally, since $\mathcal{A}$ satisfies the first conjunct of $F_n$, we have $(a,a) \not\in R_{\mathcal{A}}$ for all $a \in U_{\mathcal{A}}$. Therefore, since $(a_i,a_j) \in R_{\mathcal{A}}$, we cannot have $a_i = a_j$. This completes the proof of the claim.

    Given the claim, we have shown the existence of $n$ elements (namely $a_1,\dots,a_n$) in the universe $U_{\mathcal{A}}$, none of which are equal to any other among them. This implies that $|U_{\mathcal{A}}| \geq n$, contradicting our assumption that $|U_{\mathcal{A}}| < n$. Therefore, our assumption must be wrong, and every model satisfying $F_n$ has at least $n$ elements.
\end{proof}

\newpage

## Part (b)

\begin{theorem}
Let $\sigma$ be a signature containing only unary predicate symbols $P_1,\dots,P_k$. Let $F$ be any satisfiable $\sigma$-formula. $F$ has a model where the universe has at most $2^k$ elements.
\end{theorem}
\begin{proof}
    Let $\mathcal{A}$ be a $\sigma$-structure satisfying $F$ (exists since $F$ is satisfiable). For each $a \in U_{\mathcal{A}}$, we define a $k$-length binary string $b_a$ as:
    \begin{itemize}
        \item For each $1 \leq i \leq k$, $b_a^i=1$ if and only if $a \in P_{i\mathcal{A}}$.
    \end{itemize}

    We define a new $\sigma$-structure $\mathcal{B}$ as follows:
    \begin{itemize}
        \item $U_{\mathcal{B}} = \{b_a \mid a \in U_{\mathcal{A}}\}$, the set of $k$-length binary strings corresponding to all elements of $\mathcal{A}$.
        \item For each $1 \leq i \leq k$, $P_{i\mathcal{B}} = U_{\mathcal{B}} \bigcap (\{0,1\}^{i-1}\cdot\{1\}\cdot\{0,1\}^{k-i})$. In other words, $P_{i\mathcal{B}}$ contains exactly those strings of $U_{\mathcal{B}}$ which have $1$ at the $i$-th position.
        \item For each variable $x$, if $x_{\mathcal{A}} = a$, then $x_{\mathcal{B}} = b_a$.
    \end{itemize}

    \textbf{Claim:} The relation $\sim$ between a $\sigma$-structure $\mathcal{A}$ and the corresponding $\sigma$-structure $\mathcal{B}$ as defined above satisfies the properties mentioned in question 2.

    \textbf{Proof:}

    \begin{itemize}
        \item Any atomic formula is of the form $P_i(x)$ for some $i \in \{1,\dots,k\}$ and variable $x$. By definition, we have $\mathcal{A} \satisfies P_i(x)$ iff $x_{\mathcal{A}} \in P_{i\mathcal{A}}$ iff the string $b_{x_{\mathcal{A}}} = x_{\mathcal{B}}$ has a $1$ at the $i$-th position iff $x_{\mathcal{B}} \in P_{i\mathcal{B}}$ iff $\mathcal{B} \satisfies P_i(x)$.

        \item We have:
        \begin{itemize}
            \item For any variable $x$ and $a \in U_{\mathcal{A}}$, the $\sigma$-structure $\mathcal{B}'$ corresponding to $\mathcal{A}_{[x \;\mapsto\; a]}$ will be exactly the same as $\mathcal{B}$, except that it'll have $x_{\mathcal{B}'} = b_{a}$. Thus we wil have $\mathcal{B}' = B_{[x \;\mapsto\; b_a]}$, or in other words, $\mathcal{A}_{[x \;\mapsto\; a]} \sim \mathcal{B}_{[x \;\mapsto\; b_a]}$.
            \item Similarly, for each variable $x$ and $b_a \in U_{\mathcal{B}}$, the $\sigma$-structure $\mathcal{A}'$ which $\mathcal{B}_{[x \;\mapsto\; b_a]}$ corresponds to is exactly the same as $\mathcal{A}$, except that $x_{\mathcal{A}'} = a$. Thus we wil have $\mathcal{A}' = A_{[x \;\mapsto\; a]}$, or in other words, $\mathcal{A}_{[x \;\mapsto\; a]} \sim \mathcal{B}_{[x \;\mapsto\; b_a]}$.
        \end{itemize}
    \end{itemize}

    This completes the proof of the claim. Now, as we have proved in question 2, this implies that for any formula $G$, $\mathcal{A} \satisfies G$ iff $\mathcal{B} \satisfies G$. Since we started with the assumption that $\mathcal{A} \satisfies F$, we get $\mathcal{B} \satisfies F$. Finally, note that $U_{\mathcal{B}} \subseteq \{0,1\}^k$, i.e., all elements of $U_{\mathcal{B}}$ are $k$-length binary strings. Since there are only $2^k$ such strings, we must have $|U_{\mathcal{B}}| \leq 2^k$. Starting from an arbitrary model $\mathcal{A}$ of $F$, we have constructed a model $\mathcal{B}$ of $F$ with no more than $2^k$ elements in its universe. Therefore, any satisfiable $\sigma$-formula $F$ has a model with at most $2^k$ elements.
\end{proof}
