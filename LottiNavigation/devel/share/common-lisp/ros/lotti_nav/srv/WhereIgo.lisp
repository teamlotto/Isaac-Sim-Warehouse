; Auto-generated. Do not edit!


(cl:in-package lotti_nav-srv)


;//! \htmlinclude WhereIgo-request.msg.html

(cl:defclass <WhereIgo-request> (roslisp-msg-protocol:ros-message)
  ((request
    :reader request
    :initarg :request
    :type cl:integer
    :initform 0))
)

(cl:defclass WhereIgo-request (<WhereIgo-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WhereIgo-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WhereIgo-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lotti_nav-srv:<WhereIgo-request> is deprecated: use lotti_nav-srv:WhereIgo-request instead.")))

(cl:ensure-generic-function 'request-val :lambda-list '(m))
(cl:defmethod request-val ((m <WhereIgo-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lotti_nav-srv:request-val is deprecated.  Use lotti_nav-srv:request instead.")
  (request m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WhereIgo-request>) ostream)
  "Serializes a message object of type '<WhereIgo-request>"
  (cl:let* ((signed (cl:slot-value msg 'request)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WhereIgo-request>) istream)
  "Deserializes a message object of type '<WhereIgo-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'request) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WhereIgo-request>)))
  "Returns string type for a service object of type '<WhereIgo-request>"
  "lotti_nav/WhereIgoRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WhereIgo-request)))
  "Returns string type for a service object of type 'WhereIgo-request"
  "lotti_nav/WhereIgoRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WhereIgo-request>)))
  "Returns md5sum for a message object of type '<WhereIgo-request>"
  "bf1cfd8512ed73dbf0bc8ba1f3b6fab3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WhereIgo-request)))
  "Returns md5sum for a message object of type 'WhereIgo-request"
  "bf1cfd8512ed73dbf0bc8ba1f3b6fab3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WhereIgo-request>)))
  "Returns full string definition for message of type '<WhereIgo-request>"
  (cl:format cl:nil "int64 request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WhereIgo-request)))
  "Returns full string definition for message of type 'WhereIgo-request"
  (cl:format cl:nil "int64 request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WhereIgo-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WhereIgo-request>))
  "Converts a ROS message object to a list"
  (cl:list 'WhereIgo-request
    (cl:cons ':request (request msg))
))
;//! \htmlinclude WhereIgo-response.msg.html

(cl:defclass <WhereIgo-response> (roslisp-msg-protocol:ros-message)
  ((destination
    :reader destination
    :initarg :destination
    :type cl:string
    :initform ""))
)

(cl:defclass WhereIgo-response (<WhereIgo-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WhereIgo-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WhereIgo-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lotti_nav-srv:<WhereIgo-response> is deprecated: use lotti_nav-srv:WhereIgo-response instead.")))

(cl:ensure-generic-function 'destination-val :lambda-list '(m))
(cl:defmethod destination-val ((m <WhereIgo-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lotti_nav-srv:destination-val is deprecated.  Use lotti_nav-srv:destination instead.")
  (destination m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WhereIgo-response>) ostream)
  "Serializes a message object of type '<WhereIgo-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'destination))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'destination))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WhereIgo-response>) istream)
  "Deserializes a message object of type '<WhereIgo-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'destination) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'destination) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WhereIgo-response>)))
  "Returns string type for a service object of type '<WhereIgo-response>"
  "lotti_nav/WhereIgoResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WhereIgo-response)))
  "Returns string type for a service object of type 'WhereIgo-response"
  "lotti_nav/WhereIgoResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WhereIgo-response>)))
  "Returns md5sum for a message object of type '<WhereIgo-response>"
  "bf1cfd8512ed73dbf0bc8ba1f3b6fab3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WhereIgo-response)))
  "Returns md5sum for a message object of type 'WhereIgo-response"
  "bf1cfd8512ed73dbf0bc8ba1f3b6fab3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WhereIgo-response>)))
  "Returns full string definition for message of type '<WhereIgo-response>"
  (cl:format cl:nil "string destination~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WhereIgo-response)))
  "Returns full string definition for message of type 'WhereIgo-response"
  (cl:format cl:nil "string destination~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WhereIgo-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'destination))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WhereIgo-response>))
  "Converts a ROS message object to a list"
  (cl:list 'WhereIgo-response
    (cl:cons ':destination (destination msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'WhereIgo)))
  'WhereIgo-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'WhereIgo)))
  'WhereIgo-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WhereIgo)))
  "Returns string type for a service object of type '<WhereIgo>"
  "lotti_nav/WhereIgo")