// Auto-generated. Do not edit!

// (in-package lotti_nav.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class WhereIgoRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.request = null;
    }
    else {
      if (initObj.hasOwnProperty('request')) {
        this.request = initObj.request
      }
      else {
        this.request = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WhereIgoRequest
    // Serialize message field [request]
    bufferOffset = _serializer.int64(obj.request, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WhereIgoRequest
    let len;
    let data = new WhereIgoRequest(null);
    // Deserialize message field [request]
    data.request = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'lotti_nav/WhereIgoRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7b8b3e2da8be658e01dee48451dead03';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 request
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WhereIgoRequest(null);
    if (msg.request !== undefined) {
      resolved.request = msg.request;
    }
    else {
      resolved.request = 0
    }

    return resolved;
    }
};

class WhereIgoResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.destination = null;
    }
    else {
      if (initObj.hasOwnProperty('destination')) {
        this.destination = initObj.destination
      }
      else {
        this.destination = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WhereIgoResponse
    // Serialize message field [destination]
    bufferOffset = _serializer.string(obj.destination, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WhereIgoResponse
    let len;
    let data = new WhereIgoResponse(null);
    // Deserialize message field [destination]
    data.destination = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.destination.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'lotti_nav/WhereIgoResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8e47796db9d7d90bff30cd181ffc714b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string destination
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WhereIgoResponse(null);
    if (msg.destination !== undefined) {
      resolved.destination = msg.destination;
    }
    else {
      resolved.destination = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: WhereIgoRequest,
  Response: WhereIgoResponse,
  md5sum() { return 'bf1cfd8512ed73dbf0bc8ba1f3b6fab3'; },
  datatype() { return 'lotti_nav/WhereIgo'; }
};
