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
