;; fib(n) = fib(n-1) + fib(n-2)
(defun fibonacci (N)
" compute the N'th Fibonacci number"
	(if (or (zerop N) (= N 1))
		1
		(+ (fibonacci (- N 1)) (fibonacci (- N 2)))))
