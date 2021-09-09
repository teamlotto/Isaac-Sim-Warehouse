;; Auto-generated. Do not edit!


(when (boundp 'lotti_nav::WhereIgo)
  (if (not (find-package "LOTTI_NAV"))
    (make-package "LOTTI_NAV"))
  (shadow 'WhereIgo (find-package "LOTTI_NAV")))
(unless (find-package "LOTTI_NAV::WHEREIGO")
  (make-package "LOTTI_NAV::WHEREIGO"))
(unless (find-package "LOTTI_NAV::WHEREIGOREQUEST")
  (make-package "LOTTI_NAV::WHEREIGOREQUEST"))
(unless (find-package "LOTTI_NAV::WHEREIGORESPONSE")
  (make-package "LOTTI_NAV::WHEREIGORESPONSE"))

(in-package "ROS")





(defclass lotti_nav::WhereIgoRequest
  :super ros::object
  :slots (_request ))

(defmethod lotti_nav::WhereIgoRequest
  (:init
   (&key
    ((:request __request) 0)
    )
   (send-super :init)
   (setq _request (round __request))
   self)
  (:request
   (&optional __request)
   (if __request (setq _request __request)) _request)
  (:serialization-length
   ()
   (+
    ;; int64 _request
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _request
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _request (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _request) (= (length (_request . bv)) 2)) ;; bignum
              (write-long (ash (elt (_request . bv) 0) 0) s)
              (write-long (ash (elt (_request . bv) 1) -1) s))
             ((and (class _request) (= (length (_request . bv)) 1)) ;; big1
              (write-long (elt (_request . bv) 0) s)
              (write-long (if (>= _request 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _request s)(write-long (if (>= _request 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _request
#+(or :alpha :irix6 :x86_64)
      (setf _request (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _request (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass lotti_nav::WhereIgoResponse
  :super ros::object
  :slots (_destination ))

(defmethod lotti_nav::WhereIgoResponse
  (:init
   (&key
    ((:destination __destination) "")
    )
   (send-super :init)
   (setq _destination (string __destination))
   self)
  (:destination
   (&optional __destination)
   (if __destination (setq _destination __destination)) _destination)
  (:serialization-length
   ()
   (+
    ;; string _destination
    4 (length _destination)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _destination
       (write-long (length _destination) s) (princ _destination s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _destination
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _destination (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass lotti_nav::WhereIgo
  :super ros::object
  :slots ())

(setf (get lotti_nav::WhereIgo :md5sum-) "bf1cfd8512ed73dbf0bc8ba1f3b6fab3")
(setf (get lotti_nav::WhereIgo :datatype-) "lotti_nav/WhereIgo")
(setf (get lotti_nav::WhereIgo :request) lotti_nav::WhereIgoRequest)
(setf (get lotti_nav::WhereIgo :response) lotti_nav::WhereIgoResponse)

(defmethod lotti_nav::WhereIgoRequest
  (:response () (instance lotti_nav::WhereIgoResponse :init)))

(setf (get lotti_nav::WhereIgoRequest :md5sum-) "bf1cfd8512ed73dbf0bc8ba1f3b6fab3")
(setf (get lotti_nav::WhereIgoRequest :datatype-) "lotti_nav/WhereIgoRequest")
(setf (get lotti_nav::WhereIgoRequest :definition-)
      "int64 request
---
string destination


")

(setf (get lotti_nav::WhereIgoResponse :md5sum-) "bf1cfd8512ed73dbf0bc8ba1f3b6fab3")
(setf (get lotti_nav::WhereIgoResponse :datatype-) "lotti_nav/WhereIgoResponse")
(setf (get lotti_nav::WhereIgoResponse :definition-)
      "int64 request
---
string destination


")



(provide :lotti_nav/WhereIgo "bf1cfd8512ed73dbf0bc8ba1f3b6fab3")


