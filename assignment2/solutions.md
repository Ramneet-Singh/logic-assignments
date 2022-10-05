---
title: "**COL703 - Assignment 2**"
author:
  - name: "Ramneet Singh"
    affiliation: "2019CS50445"
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
  \usepackage{amsmath,amsfonts,amsthm,fancyhdr,float,fullpage,mathtools}
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
  \newcommand\finitesubset{\subseteq_{\text{fin}}}
  \newcommand\arrow{\supset}
  \newcommand\nat{\mathbb{N}}
  \newcommand\numberthis{\addtocounter{equation}{1}\tag{\theequation}}
  ```
pagestyle: headings
---

\newpage

# Question 1

To prove Strong Completeness, we will make use of the following four theorems. We omit their proofs since they have been covered in class.

\begin{theorem}{\textbf{(Soundness Theorem for Propositional Logic)}\\}
    \label{thm:soundness}
    Let $\alpha \in \phi$. If $\derives \alpha$ then $\satisfies \alpha$.
\end{theorem}

\begin{theorem}{\textbf{(Completeness Theorem for Propositional Logic)}\\}
    \label{thm:completeness}
    Let $\alpha \in \phi$. If $\satisfies \alpha$ then $\derives \alpha$.
\end{theorem}

\begin{theorem}{\textbf{(Deduction Theorem)}\\}
    \label{thm:deduction}
    Let $X \subseteq \phi$ and $\alpha, \beta \in \phi$. Then, $X \cup \{\alpha\} \derives \beta$ if and only if $X \derives \alpha \arrow \beta$.
\end{theorem}

\begin{theorem}{\textbf{(Compactness)}\\}
    \label{thm:compactness}
    Let $X \subseteq \phi$ and $\alpha \in \phi$. Then, $X \entails \alpha$ if and only if there exists a finite subset $Y \finitesubset X$ of $X$ such that $Y \entails \alpha$.
\end{theorem}

\begin{theorem}{\textbf{(Strong Completeness)}\\}
    Let $X \subseteq \phi$ and $\alpha \in \phi$. Then, $X \entails \alpha$ if and only if $X \derives \alpha$.
\end{theorem}
\begin{proof}
    \textbf{(if):} Assume $X \derives \alpha$. Then we can exhibit a derivation $\alpha_1, \dots, \alpha_n=\alpha$ of $\alpha$ from $X$. Let $Y$ be the set of formulas of $X$ which are actually used in the derivation, i.e., $Y = X \cap \{\alpha_1,\dots,\alpha_n\}$. From the definition of $Y$ we have $Y \finitesubset X$. Further, from the definition of $\derives$ and definition of $Y$, we have $Y \derives \alpha$ since $\alpha_1, \dots, \alpha_n=\alpha$ is also a derivation of $\alpha$ from $Y$.

    Suppose $Y = \{\beta_1, \dots, \beta_m\}$. Then, from the \hyperref[thm:deduction]{Deduction Theorem}, we have
    \begin{alignat*}{2}
        & \{\beta_1, \dots, \beta_m\} &&\derives \alpha \\
        \implies & \{\beta_1, \dots, \beta_{m-1}\} &&\derives (\beta_m \arrow \alpha) \\
        \implies & \{\beta_1, \dots, \beta_{m-2}\} &&\derives (\beta_{m-1} \arrow (\beta_m \arrow \alpha)) \\
                & &&\vdots \\
        \implies & &&\derives (\beta_1 \arrow (\beta_2 \arrow ( \dots (\beta_m \arrow \alpha) \dots )))
    \end{alignat*}

    From the \hyperref[thm:soundness]{Soundness Theorem for Propositional Logic}, $\derives (\beta_1 \arrow (\beta_2 \arrow ( \dots (\beta_m \arrow \alpha) \dots )))$ implies 
    $$\satisfies (\beta_1 \arrow (\beta_2 \arrow ( \dots (\beta_m \arrow \alpha) \dots )))$$ 
    We claim that this implies $\{\beta_1,\beta_2,\dots,\beta_m\} \entails \alpha$. The claim holds because if it didn't, then we would have a valuation $v$ such that $v(\beta_1)=\dots=v(\beta_m)=\top$ and $v(\alpha)=\bot$. But then we would have $v(\beta_1 \arrow (\beta_2 \arrow ( \dots (\beta_m \arrow \alpha) \dots ))) = \bot$, which is a contradiction (since $\satisfies (\beta_1 \arrow (\beta_2 \arrow ( \dots (\beta_m \arrow \alpha) \dots )))$). So, $Y = \{\beta_1, \dots, \beta_m\}$ is a finite subset of $X$ such that $Y \entails \alpha$. From \hyperref[thm:compactness]{Compactness}, this implies that $X \entails \alpha$. \\

    \textbf{(Only If):} Assume $X \entails \alpha$. From \hyperref[thm:compactness]{Compactness}, this implies that there is a finite subset $Y \finitesubset X$ such that $Y \entails \alpha$. Suppose $Y = \{\beta_1, \dots, \beta_m\}$. Then we have $\{\beta_1, \dots, \beta_m\} \entails \alpha$. This implies that $\entails (\beta_1 \arrow (\beta_2 \arrow ( \dots (\beta_m \arrow \alpha) )))$ holds (if it didn't, then we would have a valuation $v$ in which $v(\beta_1)=\dots=v(\beta_m)=\top$ and $v(\alpha)=\bot$, which is not possible since $\{\beta_1, \dots, \beta_m\} \entails \alpha$). From the \hyperref[thm:completeness]{Completeness Theorem for Propositional Logic}, this implies $\derives (\beta_1 \arrow (\beta_2 \arrow ( \dots (\beta_m \arrow \alpha) \dots )))$. From the \hyperref[thm:deduction]{Deduction Theorem}, we have
    \begin{alignat*}{2}
        & &&\derives (\beta_1 \arrow (\beta_2 \arrow ( \dots (\beta_m \arrow \alpha) \dots ))) \\
        \implies & \{\beta_1\} &&\derives (\beta_2 \arrow ( \dots (\beta_m \arrow \alpha) \dots )) \\
        \implies & \{\beta_1, \beta_2\} &&\derives (\beta_3 \arrow \dots (\beta_m \arrow \alpha) \dots ) \\
                & &&\vdots \\
        \implies & \{\beta_1, \dots, \beta_m\} &&\derives \alpha \numberthis \label{eq:1}
    \end{alignat*}

    Since $\{\beta_1, \dots, \beta_m\} \subseteq X$, from the definition of $\derives$, equation \ref{eq:1} implies that $X \derives \alpha$.
\end{proof}

\newpage

# Question 2

## Part (a)

\begin{theorem}
    \label{thm:extend-maximal}
    Every FSS can be extended to a maximal FSS.
\end{theorem}
\begin{proof}
    Let $X$ be an arbitrary FSS. Let $\{\alpha_0, \alpha_1, \dots \}$ be an enumeration of $\phi$.

    We define an infinite sequence of sets $X_0, X_1, X_2, \dots$ as follows.
    \begin{itemize}
        \item $X_0 = X$
        \item For $i \geq 0$, $X_{i+1} = \begin{cases*}
                                X_i \cup \{\alpha_i\} & if $X_i \cup \{\alpha_i\}$ is an FSS \\
                                X_i        & otherwise
                                \end{cases*}$
    \end{itemize}

    Let $Y = \bigcup_{i \in \nat}{X_i}$. By definition, we have that each $X_i$ is an FSS and $X_0 \subseteq X_1 \subseteq \dots \subseteq Y$. We claim that $Y$ is a maximal FSS that extends $X$. Firstly, note that since $X = X_0 \subseteq Y$, it extends $X$.

    Secondly, we will show that $Y$ is an FSS. Assume, for the sake of contradiction, that it is not. Then there exists a finite subset $Z = \{\beta_1, \beta_2, \dots, \beta_n \}$ of $Y$ which is not satisfiable. Let the formulas of $Z$ in our enumeration of $\phi$ be $\{\alpha_{i_1}, \alpha_{i_2}, \dots, \alpha_{i_n} \}$. We then have that $Z \finitesubset X_{j+1}$, where $j = \operatorname{max}(i_1,i_2,\dots,i_n)$. Since $Z$ is not satisfiable, this implies that $X_{j+1}$ is not an FSS, which is a contradiction (as every $X_i$ is an FSS by definition).

    Thirdly, we will show that $Y$ is a maximal FSS. Assume, for the sake of contradiction, that it is not. Then there exists $\beta \not\in Y$ such that $Y \cup \{\beta\}$ is also an FSS. Let $\beta = \alpha_j$ in our enumeration. Since $\alpha_j \not\in Y$, $\alpha_j$ wasn't added at step $j+1$ in our construction. This means that $X_j \cup \{\alpha_j\}$ is not an FSS. Therefore, there exists a finite subset $Z \finitesubset X_j \cup \{\alpha_j\}$ which is not satisfiable. Since $X_j \subseteq Y$, we also have $Z \finitesubset Y \cup \{\alpha_j\}$. So $Z$ being not satisfiable is a contradiction since we had assumed that $Y \cup \{\alpha_j\} = Y \cup \{\beta\}$ is an FSS and every finite subset of an FSS is satisfiable. Hence, our assumption must have been wrong, and $Y$ is a maximal FSS.
\end{proof}

\newpage

## Part (b)

\begin{theorem}
    \label{thm:fss-prop-1}
    Let $X$ be a maximal FSS. Then, for every formula $\alpha$, $\alpha \in X$ if and only if $\neg \alpha \not\in X$.
\end{theorem}
\begin{proof}
    Let $\alpha$ be any formula. First, we will show that $\alpha$ and $\neg \alpha$ cannot both be in $X$, i.e., that we cannot have $\{\alpha,\neg\alpha\} \subseteq X$. To see why, note that the set $\{\alpha, \neg \alpha\}$ is not satisfiable since for any valuation $v$, $v(\alpha) = \top$ if and only if $v(\neg \alpha) = \bot$. Since $X$ is an FSS, there exists no subset of $X$ which is not satisfiable. Therefore, $\{\alpha,\neg\alpha\}$ cannot be a subset of $X$, i.e., $\alpha$ and $\neg\alpha$ cannot both belong to $X$.

    Second, we will show that at least one of $\alpha$ and $\neg \alpha$ must be in $X$. This proof is by contradiction. Assume, if possible, that $\alpha \not\in X$ and $\neg \alpha \not\in X$. Since $X$ is a \emph{maximal} FSS, this implies that there exist finite subsets $B \finitesubset X$ and $C \finitesubset X$ such that $B \cup \{\alpha\}$ is not satisfiable and $C \cup \{\neg\alpha\}$ is not satisfiable. Let $B = \{ \beta_1, \beta_2, \dots, \beta_n \}$ and $C = \{\gamma_1, \gamma_2, \dots, \gamma_m\}$. Let $\widehat{\beta}$ abbreviate the formula $\beta_1 \land \beta_2 \land \dots \land \beta_n$ and $\widehat{\gamma}$ abbreviate the formula $\gamma_1 \land \gamma_2 \land \dots \land \gamma_m$ Since $B \cup \{\alpha\}$ is not satisfiable, we have that $\neg (\widehat{\beta} \land \alpha)$ is valid. Since $C \cup \{\neg\alpha\}$ is not satisfiable, we have that $\neg(\widehat{\gamma} \land \neg\alpha)$ is valid. In other words, we have $\vDash \neg(\widehat{\beta} \land \alpha)$ and $\vDash \neg(\widehat{\gamma} \land \neg \alpha)$. Rewriting using DeMorgan's Laws, we have $\vDash \neg\widehat{\beta} \lor \neg\alpha$ and $\vDash \neg\widehat{\gamma} \lor \alpha$. Now, for any valuation $v$,
    \begin{itemize}
        \item If $v(\alpha)=\top$, $\vDash \neg\widehat{\beta} \lor \neg\alpha$ gives us $v(\neg\widehat{\beta})=\top$.
        \item If $v(\alpha)=\bot$, $\vDash \neg\widehat{\gamma} \lor \alpha$ gives us $v(\neg\widehat{\gamma})=\top$.
    \end{itemize}
 
    In either case, we will have $v(\neg\widehat{\beta} \lor \neg\widehat{\gamma})=\top$. Since this holds for any valuation, we can conclude $\vDash \neg\widehat{\beta} \lor \neg\widehat{\gamma}$. Rewriting using DeMorgan's Laws, we get $\vDash \neg(\widehat{\beta} \land \widehat{\gamma})$. This implies that the set $B \cup C$ is not satisfiable. Since $B,C \finitesubset X$, we have that $B \cup C \finitesubset X$ is a finite subset of $X$ which is not satisfiable, contradicting the fact that $X$ is an FSS. Therefore, our assumption must be wrong, and at least one of $\alpha,\neg\alpha$ must be in $X$.

    Since both cannot be in $X$ together and at least one must be there, if $\alpha \in X$ then $\neg \alpha$ cannot be in $X$ and if $\neg \alpha \not \in X$ then $\alpha$ must be in $X$. This completes the proof.
\end{proof}

\newpage

## Part (c)

\begin{theorem}
    \label{thm:fss-prop-2}
    Let $X$ be a maximal FSS. For all formulas $\alpha,\beta$, $(\alpha \lor \beta) \in X$ if and only if ($\alpha \in X$ or $\beta \in X$).
\end{theorem}
\begin{proof}
    Let $\alpha,\beta$ be two arbitrary formulas. We will show that $\alpha \lor \beta \in X$ if and only if $\alpha \in X$ or $\beta \in X$.

    \textbf{(If):} Assume, without loss of generality, that $\alpha \in X$. We will show that $\alpha \lor \beta \in X$. The proof is by contradiction. Assume, if possible, that $\alpha \lor \beta \not\in X$. Since $X$ is a maximal FSS, this implies that there exists a finite subset $Y \finitesubset X$ such that $Y \cup \{\alpha \lor \beta\}$ is not satisfiable. Let $Y = \{\alpha_1, \dots, \alpha_n\}$ and let $\widehat{\alpha}$ abbreviate the formula $\alpha_1 \land \alpha_2 \land \dots \land \alpha_n$. $Y \cup \{\alpha \lor \beta\}$ is not satisfiable means that $\neg(\widehat{\alpha} \land (\alpha \lor \beta))$ is valid, i.e., we have $\vDash \neg(\widehat{\alpha} \land (\alpha \lor \beta))$. We have

    \begin{alignat*}{2}
        \vDash& \neg(\widehat{\alpha} \land (\alpha \lor \beta)) && \\
        \implies \vDash& \neg((\widehat{\alpha} \land \alpha) \lor (\widehat{\alpha} \land \beta)) &&\;\;\text{(Distributivity)} \\
        \implies \vDash& \neg(\widehat{\alpha} \land \alpha) \land \neg(\widehat{\alpha} \land \beta) &&\;\;\text{(DeMorgan's Laws)} \\
        \implies \vDash& \neg(\widehat{\alpha} \land \alpha) &&\;\;\text{(Defn. of } \land \text{)} \numberthis \label{eq:2}
    \end{alignat*}

    Equation \ref{eq:2} implies that the set $Y \cup \{\alpha\}$ is not satisfiable. But $Y \finitesubset X$ and $\alpha \in X$, so $Y \cup \{\alpha\} \finitesubset X$ is a finite subset of $X$ which is not satisfiable, contradicting the fact that $X$ is an FSS. So our assumption must have been wrong, and we have $\alpha \lor \beta \in X$.

    \textbf{(Only If):} Assume $(\alpha \lor \beta) \in X$. We will show that $\alpha \in X$ or $\beta \in X$. The proof is by contradiction. Assume, for the sake of contradiction, that $\alpha \not\in X$ and $\beta \not\in X$. Since $X$ is a maximal FSS, this implies that there exist finite subsets $B,C \finitesubset X$ of $X$ such that $B \cup \{\alpha\}$ is not satisfiable and $C \cup \{\beta\}$ is not satisfiable. Let $B = \{ \beta_1, \beta_2, \dots, \beta_n \}$ and $C = \{\gamma_1, \gamma_2, \dots, \gamma_m\}$. Let $\widehat{\beta}$ abbreviate the formula $\beta_1 \land \beta_2 \land \dots \land \beta_n$ and $\widehat{\gamma}$ abbreviate the formula $\gamma_1 \land \gamma_2 \land \dots \land \gamma_m$ Since $B \cup \{\alpha\}$ is not satisfiable, we have that $\neg (\widehat{\beta} \land \alpha)$ is valid. Since $C \cup \{\beta\}$ is not satisfiable, we have that $\neg(\widehat{\gamma} \land \beta)$ is valid. In other words, we have $\vDash \neg(\widehat{\beta} \land \alpha)$ and $\vDash \neg(\widehat{\gamma} \land \beta)$. Rewriting using DeMorgan's Laws, we have $\vDash \neg\widehat{\beta} \lor \neg\alpha$ and $\vDash \neg\widehat{\gamma} \lor \neg\beta$. We claim that
        $$
        \vDash \neg\widehat{\beta} \lor \neg\widehat{\gamma} \lor (\neg\alpha \land \neg\beta)
        $$
    To see why, consider an arbitrary valuation $v$. We have two cases:
    \begin{itemize}
        \item If $v(\neg\widehat{\beta}) = \top$ or $v(\neg\widehat{\gamma})=\top$, then $v \vDash \neg\widehat{\beta} \lor \neg\widehat{\gamma} \lor (\neg\alpha \land \neg\beta)$.
        \item If neither is true, then $\vDash \neg\widehat{\beta} \lor \neg\alpha$ and $\vDash \neg\widehat{\gamma} \lor \neg\beta$ tell us that we must have $v \vDash \neg\alpha$ and $v \vDash \neg\beta$. So, we will have $v \vDash (\neg\alpha \land \neg\beta)$ and thus $v \vDash \neg\widehat{\beta} \lor \neg\widehat{\gamma} \lor (\neg\alpha \land \neg\beta)$.
    \end{itemize}
    Therefore, we have $\vDash \neg\widehat{\beta} \lor \neg\widehat{\gamma} \lor (\neg\alpha \land \neg\beta)$. Rewriting this using DeMorgan's Laws, we get $\vDash \neg\widehat{\beta} \lor \neg\widehat{\gamma} \lor \neg(\alpha \lor \beta)$. Again rewriting using DeMorgan's Laws, we get $\vDash \neg(\widehat{\beta} \land \widehat{\gamma} \land (\alpha \lor \beta))$. This implies that the set $B \cup C \cup \{\alpha \lor \beta\}$ is not satisfiable. Since $B,C \finitesubset X$ and $\alpha \lor \beta \in X$, we have that $B \cup C \cup \{\alpha \lor \beta \} \finitesubset X$ is a finite subset of $X$ which is not satisfiable, contradicting the fact that $X$ is an FSS. Therefore, our assumption must be wrong, and we have $\alpha \in X$ or $\beta \in X$.
\end{proof}

\newpage

## Part (d)

Let $X$ be an arbitrary maximal FSS. Define the valuation $v_X$ as setting every atomic proposition in $X$ (and only the atomic propositions in $X$) to true. Formally, $v_X = \{ p \in \mathcal{P} \mid p \in X \}$ or in other words, $v(p) = \top$ *iff* $p \in X$. We will now show that the valuation $v_X$ has the property mentioned in Question 2(d). We have the following theorem:

\begin{theorem}
    \label{thm:sat-valuation}
    For all formulas $\alpha$, $v_X \vDash \alpha$ if and only if $\alpha \in X$.
\end{theorem}
\begin{proof}
    The proof is by structural induction on $\alpha$.

    \textbf{Base Case:} $\alpha = p$, a propositional atom. We have $v_X \vDash p$ iff $v_X(p) = \top$. By the definition of $v_X$, this happens iff $p \in X$.
    
    \textbf{Induction Step:} We have the following two cases:
    \begin{itemize}
        \item $\alpha = \neg \beta$. We have
        \begin{alignat*}{2}
            & v_X \vDash \alpha && \\
            \text{iff}&\; v_X \not\vDash \beta && \text{(by defn. of valuations)} \\
            \text{iff}&\; \beta \not\in X && \text{(by induction hypothesis)} \\
            \text{iff}&\; \neg\beta \in X && \text{(by theorem \ref{thm:fss-prop-1})} \\
            \text{iff}&\; \alpha \in X && \text{(} \alpha=\neg\beta \text{)}
        \end{alignat*}

        \item $\alpha = \beta \lor \gamma$. We have
        \begin{alignat*}{2}
            & v_X \vDash \alpha && \\
            \text{iff}&\; v_X \vDash \beta \text{ or } v_X \vDash \gamma && \text{(by defn. of valuations)} \\
            \text{iff}&\; \beta \in X \text{ or } \gamma \in X && \text{(by induction hypothesis)} \\
            \text{iff}&\; \beta \lor \gamma \in X && \text{(by theorem \ref{thm:fss-prop-2})} \\
            \text{iff}&\; \alpha \in X && \text{(} \alpha=\beta \lor \gamma \text{)}
        \end{alignat*}
    \end{itemize}
    In both cases, $v_X \vDash \alpha$ if and only if $\alpha \in X$. This completes the induction step and our proof.
\end{proof}

We had started with an arbitrary maximal FSS $X$, and we have shown a valuation $v_X$ which has the desired property. Therefore, every maximal FSS $X$ generates a valuation $v_X$ such that for every formula $\alpha$, $v_X \vDash \alpha$ iff $\alpha \in X$.

\newpage

## Part (e)

We will now show that every FSS $X$ is simultaneously satisfiable. Formally, we have the following theorem.

\begin{theorem}
    \label{thm:fss-sat}
    Let $X$ be an FSS. There exists a valuation $v$ such that $v \vDash X$.
\end{theorem}
\begin{proof}
    From theorem \ref{thm:extend-maximal}, $X$ can be extended to a maximal FSS $X'$. Let $v_{X'}$ be the valuation generated by $X'$, i.e., $v_{X'}(p) = \top$ iff $p \in X'$. Now, take an arbitrary formula $\alpha \in X$. Since $X'$ extends $X$, we have $\alpha \in X'$. Then, from theorem \ref{thm:sat-valuation}, this implies that $v_{X'} \vDash \alpha$. Since $\alpha$ was arbitrary, we can conclude $v_{X'} \vDash \beta$ for all $\beta \in X$, i.e., $v_{X'} \vDash X$. So we have shown the existence of such a valuation.
\end{proof}

\newpage

## Part (f)

Before proving the main theorem, we prove a lemma which will help us.

\begin{lemma}
    \label{lem:entail-sat}
    Let $Z \subseteq \phi$ and $\beta \in \phi$. $Z \vDash \beta$ if and only if $Z \cup \{\neg\beta\}$ is not satisfiable.
\end{lemma}
\begin{proof}
    \textbf{(If):} Suppose that $Z \cup \{\neg\beta\}$ is not satisfiable. Then, we will show that $Z \vDash \beta$. The proof is by contradiction. Assume, for the sake of contradiction, that $Z \not\vDash \beta$. Then there exists a valuation $v$ such that $v \vDash Z$ but $v \not\vDash \beta$. Since $v \not\vDash \beta$, $v \vDash \neg\beta$. Since $v \vDash Z$ and $v \vDash \neg\beta$, we have $v \vDash Z \cup \{\neg\beta\}$. This is a contradiction to the fact that $Z \cup \{\neg\beta\}$ is not satisfiable. Therefore, our assumption must be wrong, and we have $Z \vDash \beta$.

    \textbf{(Only If):} Suppose that $Z \vDash \beta$. Then, we will show that $Z \cup \{\neg\beta\}$ is not satisfiable. The proof is by contradiction. Assume, for the sake of contradiction, that $Z \cup \{\neg\beta\}$ is satisfiable. Then there exists a valuation $v$ such that $v \vDash Z \cup \{\neg\beta\}$. This implies that $v \vDash Z$ and $v \vDash \neg\beta$. Since $v \vDash \neg\beta$, $v \not\vDash \beta$. So we have $v \vDash Z$ and $v \not\vDash \beta$, which is a contradiction to the fact that $Z \vDash \beta$. Therefore, our assumption must be wrong, and $Z \cup \{\neg\beta\}$ is not satisfiable.
\end{proof}

\begin{theorem}
    Let $X \subseteq \phi$, $\alpha \in \phi$. $X \vDash \alpha$ iff there exists $Y \finitesubset X$ such that $Y \vDash \alpha$.
\end{theorem}
\begin{proof}
    \textbf{(If):} Assume there exists $Y \finitesubset X$ such that $Y \vDash \alpha$. To show that $X \vDash \alpha$, we have to show that for any valuation $v$, $v \vDash X$ implies $v \vDash \alpha$. Let $v$ be an arbitrary valuation. If $v \vDash X$, then $v \vDash \beta$ for every $\beta \in X$. Since $Y \subseteq X$, $v \vDash \beta$ for every $\beta \in Y$, so we have $v \vDash Y$. Since $Y \vDash \alpha$, this implies that $v \vDash \alpha$. For any valuation $v$, we have shown that if $v \vDash X$ then $v \vDash \alpha$ (if there is no valuation $v$ such that $v \vDash X$ then this holds vacuously). So we can conclude $X \vDash \alpha$.

    \textbf{(Only If):} Assume $X \vDash \alpha$. We will show that there exists a finite subset $Z \finitesubset X$ of $X$ such that $Z \vDash \alpha$. From lemma \ref{lem:entail-sat}, $X \vDash \alpha$ implies that $X \cup \{\neg\alpha\}$ is not satisfiable. Now, since $X \cup \{\neg\alpha\}$ is not satisfiable, we claim that $X \cup \{\neg\alpha\}$ is not an FSS. This claim holds because if it were an FSS, then from theorem \ref{thm:fss-sat}, we would have a satisfying valuation. Since it is not an FSS, by the definition of an FSS, there exists a finite subset $Y \finitesubset X \cup \{\neg\alpha\}$ such that $Y$ is not satisfiable. Then, $(Y \setminus \{\neg\alpha\}) \cup \{\neg\alpha\}$ is not satisfiable either, where $(Y \setminus \{\neg\alpha\}) \finitesubset X$. From lemma \ref{lem:entail-sat}, this implies that $(Y \setminus \{\neg\alpha\}) \vDash \alpha$. So there exists a finite subset $Z$ of $X$ such that $Z \vDash \alpha$ (namely, $(Y \setminus \{\neg\alpha\})$ is such a set). This completes the proof.
\end{proof}
