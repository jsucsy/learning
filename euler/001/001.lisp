;jsu
;create 16 Dec 2012
;last edit 16 Dec 2012
;***not a correct solution, outputs 45 for limit = 10

(defun check_mod(i x y)
  (or (= (mod i x) 0) (= (mod i y) 0)))

(defun check_multiple(x y limit)
	(loop for i from 1 below limit 
		do (when (check_mod i x y))
		sum i))

;	(loop for i from 1 below limit do (print (or((mod i x) 0) ((mod i y) 0))))
;	)