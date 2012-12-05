;;; testing.lisp
;;; by jsu

;; Triple value of a number

(defun triple (X)
	"Compute three times X." ;inline comment here
	(* 3 X))


;; Negate sign of number
(defun negate (X)
	"Negate the value of X."
	(- X))

;; recursive factorial definition
(defun factorial (N)
	"Compute the factorial of N."
	(if (= N 1)
		1
	      (* N (factorial (- N 1 )))))

;; increment global and multiply definition
(defun increment-global-and-multiply (by-me)
	(setf my-global-counter (1+ my-global-counter))
	(* my-global-counter by-me))

;; triangular number is 1 + 2 + 3 + ... + N
(defun triangular (N)
	"Compute the triangular of N"
	(if (= N 1)
		1
		(+ N(triangular(- N 1)))))

;; raise B to the power E
(defun power (B E)
	(if (= E 1)
		B
		(* B(power B (- E 1)))))

;; fib(n) = fib(n-1) + fib(n-2)
(defun fibonacci (N)
" compute the N'th Fibonacci number"
	(if (or (zerop N) (= N 1))
		1
		(+ (fibonacci (- N 1)) (fibonacci (- N 2)))))
