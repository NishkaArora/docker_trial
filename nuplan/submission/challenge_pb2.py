# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: challenge.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='challenge.proto',
  package='challenge_protocol',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63hallenge.proto\x12\x12\x63hallenge_protocol\"\x07\n\x05\x45mpty\"u\n\x17SimulationHistoryBuffer\x12\x12\n\nego_states\x18\x01 \x03(\x0c\x12\x14\n\x0cobservations\x18\x02 \x03(\x0c\x12\x1c\n\x0fsample_interval\x18\x03 \x01(\x02H\x00\x88\x01\x01\x42\x12\n\x10_sample_interval\"5\n\x13SimulationIteration\x12\x0f\n\x07time_us\x18\x01 \x01(\x03\x12\r\n\x05index\x18\x02 \x01(\x05\"-\n\x16TrafficLightStatusType\x12\x13\n\x0bstatus_name\x18\x01 \x01(\t\"\x82\x01\n\x16TrafficLightStatusData\x12:\n\x06status\x18\x01 \x01(\x0b\x32*.challenge_protocol.TrafficLightStatusType\x12\x19\n\x11lane_connector_id\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"\xed\x01\n\x0cPlannerInput\x12\x45\n\x14simulation_iteration\x18\x01 \x01(\x0b\x32\'.challenge_protocol.SimulationIteration\x12N\n\x19simulation_history_buffer\x18\x02 \x01(\x0b\x32+.challenge_protocol.SimulationHistoryBuffer\x12\x46\n\x12traffic_light_data\x18\x03 \x03(\x0b\x32*.challenge_protocol.TrafficLightStatusData\"1\n\x08StateSE2\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x0f\n\x07heading\x18\x03 \x01(\x02\"%\n\rStateVector2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\x7f\n\x1aPlannerInitializationLight\x12\x1b\n\x13route_roadblock_ids\x18\x01 \x03(\t\x12\x32\n\x0cmission_goal\x18\x02 \x01(\x0b\x32\x1c.challenge_protocol.StateSE2\x12\x10\n\x08map_name\x18\x03 \x01(\t\"\xa2\x02\n\x08\x45goState\x12\x34\n\x0erear_axle_pose\x18\x01 \x01(\x0b\x32\x1c.challenge_protocol.StateSE2\x12@\n\x15rear_axle_velocity_2d\x18\x02 \x01(\x0b\x32!.challenge_protocol.StateVector2D\x12\x44\n\x19rear_axle_acceleration_2d\x18\x03 \x01(\x0b\x32!.challenge_protocol.StateVector2D\x12\x1b\n\x13tire_steering_angle\x18\x04 \x01(\x02\x12\x0f\n\x07time_us\x18\x05 \x01(\x03\x12\x13\n\x0b\x61ngular_vel\x18\x06 \x01(\x02\x12\x15\n\rangular_accel\x18\x07 \x01(\x02\">\n\nTrajectory\x12\x30\n\nego_states\x18\x01 \x03(\x0b\x32\x1c.challenge_protocol.EgoState2\xd5\x01\n\x18\x44\x65tectionTracksChallenge\x12`\n\x11InitializePlanner\x12..challenge_protocol.PlannerInitializationLight\x1a\x19.challenge_protocol.Empty\"\x00\x12W\n\x11\x43omputeTrajectory\x12 .challenge_protocol.PlannerInput\x1a\x1e.challenge_protocol.Trajectory\"\x00\x62\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='challenge_protocol.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=46,
)


_SIMULATIONHISTORYBUFFER = _descriptor.Descriptor(
  name='SimulationHistoryBuffer',
  full_name='challenge_protocol.SimulationHistoryBuffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ego_states', full_name='challenge_protocol.SimulationHistoryBuffer.ego_states', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='observations', full_name='challenge_protocol.SimulationHistoryBuffer.observations', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_interval', full_name='challenge_protocol.SimulationHistoryBuffer.sample_interval', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_sample_interval', full_name='challenge_protocol.SimulationHistoryBuffer._sample_interval',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=48,
  serialized_end=165,
)


_SIMULATIONITERATION = _descriptor.Descriptor(
  name='SimulationIteration',
  full_name='challenge_protocol.SimulationIteration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_us', full_name='challenge_protocol.SimulationIteration.time_us', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='challenge_protocol.SimulationIteration.index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=220,
)


_TRAFFICLIGHTSTATUSTYPE = _descriptor.Descriptor(
  name='TrafficLightStatusType',
  full_name='challenge_protocol.TrafficLightStatusType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_name', full_name='challenge_protocol.TrafficLightStatusType.status_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=267,
)


_TRAFFICLIGHTSTATUSDATA = _descriptor.Descriptor(
  name='TrafficLightStatusData',
  full_name='challenge_protocol.TrafficLightStatusData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='challenge_protocol.TrafficLightStatusData.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_connector_id', full_name='challenge_protocol.TrafficLightStatusData.lane_connector_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='challenge_protocol.TrafficLightStatusData.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=400,
)


_PLANNERINPUT = _descriptor.Descriptor(
  name='PlannerInput',
  full_name='challenge_protocol.PlannerInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='simulation_iteration', full_name='challenge_protocol.PlannerInput.simulation_iteration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='simulation_history_buffer', full_name='challenge_protocol.PlannerInput.simulation_history_buffer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='traffic_light_data', full_name='challenge_protocol.PlannerInput.traffic_light_data', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=640,
)


_STATESE2 = _descriptor.Descriptor(
  name='StateSE2',
  full_name='challenge_protocol.StateSE2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='challenge_protocol.StateSE2.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='challenge_protocol.StateSE2.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heading', full_name='challenge_protocol.StateSE2.heading', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=642,
  serialized_end=691,
)


_STATEVECTOR2D = _descriptor.Descriptor(
  name='StateVector2D',
  full_name='challenge_protocol.StateVector2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='challenge_protocol.StateVector2D.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='challenge_protocol.StateVector2D.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=693,
  serialized_end=730,
)


_PLANNERINITIALIZATIONLIGHT = _descriptor.Descriptor(
  name='PlannerInitializationLight',
  full_name='challenge_protocol.PlannerInitializationLight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='route_roadblock_ids', full_name='challenge_protocol.PlannerInitializationLight.route_roadblock_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mission_goal', full_name='challenge_protocol.PlannerInitializationLight.mission_goal', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map_name', full_name='challenge_protocol.PlannerInitializationLight.map_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=732,
  serialized_end=859,
)


_EGOSTATE = _descriptor.Descriptor(
  name='EgoState',
  full_name='challenge_protocol.EgoState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rear_axle_pose', full_name='challenge_protocol.EgoState.rear_axle_pose', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rear_axle_velocity_2d', full_name='challenge_protocol.EgoState.rear_axle_velocity_2d', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rear_axle_acceleration_2d', full_name='challenge_protocol.EgoState.rear_axle_acceleration_2d', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tire_steering_angle', full_name='challenge_protocol.EgoState.tire_steering_angle', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_us', full_name='challenge_protocol.EgoState.time_us', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angular_vel', full_name='challenge_protocol.EgoState.angular_vel', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angular_accel', full_name='challenge_protocol.EgoState.angular_accel', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=862,
  serialized_end=1152,
)


_TRAJECTORY = _descriptor.Descriptor(
  name='Trajectory',
  full_name='challenge_protocol.Trajectory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ego_states', full_name='challenge_protocol.Trajectory.ego_states', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1154,
  serialized_end=1216,
)

_SIMULATIONHISTORYBUFFER.oneofs_by_name['_sample_interval'].fields.append(
  _SIMULATIONHISTORYBUFFER.fields_by_name['sample_interval'])
_SIMULATIONHISTORYBUFFER.fields_by_name['sample_interval'].containing_oneof = _SIMULATIONHISTORYBUFFER.oneofs_by_name['_sample_interval']
_TRAFFICLIGHTSTATUSDATA.fields_by_name['status'].message_type = _TRAFFICLIGHTSTATUSTYPE
_PLANNERINPUT.fields_by_name['simulation_iteration'].message_type = _SIMULATIONITERATION
_PLANNERINPUT.fields_by_name['simulation_history_buffer'].message_type = _SIMULATIONHISTORYBUFFER
_PLANNERINPUT.fields_by_name['traffic_light_data'].message_type = _TRAFFICLIGHTSTATUSDATA
_PLANNERINITIALIZATIONLIGHT.fields_by_name['mission_goal'].message_type = _STATESE2
_EGOSTATE.fields_by_name['rear_axle_pose'].message_type = _STATESE2
_EGOSTATE.fields_by_name['rear_axle_velocity_2d'].message_type = _STATEVECTOR2D
_EGOSTATE.fields_by_name['rear_axle_acceleration_2d'].message_type = _STATEVECTOR2D
_TRAJECTORY.fields_by_name['ego_states'].message_type = _EGOSTATE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['SimulationHistoryBuffer'] = _SIMULATIONHISTORYBUFFER
DESCRIPTOR.message_types_by_name['SimulationIteration'] = _SIMULATIONITERATION
DESCRIPTOR.message_types_by_name['TrafficLightStatusType'] = _TRAFFICLIGHTSTATUSTYPE
DESCRIPTOR.message_types_by_name['TrafficLightStatusData'] = _TRAFFICLIGHTSTATUSDATA
DESCRIPTOR.message_types_by_name['PlannerInput'] = _PLANNERINPUT
DESCRIPTOR.message_types_by_name['StateSE2'] = _STATESE2
DESCRIPTOR.message_types_by_name['StateVector2D'] = _STATEVECTOR2D
DESCRIPTOR.message_types_by_name['PlannerInitializationLight'] = _PLANNERINITIALIZATIONLIGHT
DESCRIPTOR.message_types_by_name['EgoState'] = _EGOSTATE
DESCRIPTOR.message_types_by_name['Trajectory'] = _TRAJECTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.Empty)
  })
_sym_db.RegisterMessage(Empty)

SimulationHistoryBuffer = _reflection.GeneratedProtocolMessageType('SimulationHistoryBuffer', (_message.Message,), {
  'DESCRIPTOR' : _SIMULATIONHISTORYBUFFER,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.SimulationHistoryBuffer)
  })
_sym_db.RegisterMessage(SimulationHistoryBuffer)

SimulationIteration = _reflection.GeneratedProtocolMessageType('SimulationIteration', (_message.Message,), {
  'DESCRIPTOR' : _SIMULATIONITERATION,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.SimulationIteration)
  })
_sym_db.RegisterMessage(SimulationIteration)

TrafficLightStatusType = _reflection.GeneratedProtocolMessageType('TrafficLightStatusType', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICLIGHTSTATUSTYPE,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.TrafficLightStatusType)
  })
_sym_db.RegisterMessage(TrafficLightStatusType)

TrafficLightStatusData = _reflection.GeneratedProtocolMessageType('TrafficLightStatusData', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICLIGHTSTATUSDATA,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.TrafficLightStatusData)
  })
_sym_db.RegisterMessage(TrafficLightStatusData)

PlannerInput = _reflection.GeneratedProtocolMessageType('PlannerInput', (_message.Message,), {
  'DESCRIPTOR' : _PLANNERINPUT,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.PlannerInput)
  })
_sym_db.RegisterMessage(PlannerInput)

StateSE2 = _reflection.GeneratedProtocolMessageType('StateSE2', (_message.Message,), {
  'DESCRIPTOR' : _STATESE2,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.StateSE2)
  })
_sym_db.RegisterMessage(StateSE2)

StateVector2D = _reflection.GeneratedProtocolMessageType('StateVector2D', (_message.Message,), {
  'DESCRIPTOR' : _STATEVECTOR2D,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.StateVector2D)
  })
_sym_db.RegisterMessage(StateVector2D)

PlannerInitializationLight = _reflection.GeneratedProtocolMessageType('PlannerInitializationLight', (_message.Message,), {
  'DESCRIPTOR' : _PLANNERINITIALIZATIONLIGHT,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.PlannerInitializationLight)
  })
_sym_db.RegisterMessage(PlannerInitializationLight)

EgoState = _reflection.GeneratedProtocolMessageType('EgoState', (_message.Message,), {
  'DESCRIPTOR' : _EGOSTATE,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.EgoState)
  })
_sym_db.RegisterMessage(EgoState)

Trajectory = _reflection.GeneratedProtocolMessageType('Trajectory', (_message.Message,), {
  'DESCRIPTOR' : _TRAJECTORY,
  '__module__' : 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:challenge_protocol.Trajectory)
  })
_sym_db.RegisterMessage(Trajectory)



_DETECTIONTRACKSCHALLENGE = _descriptor.ServiceDescriptor(
  name='DetectionTracksChallenge',
  full_name='challenge_protocol.DetectionTracksChallenge',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1219,
  serialized_end=1432,
  methods=[
  _descriptor.MethodDescriptor(
    name='InitializePlanner',
    full_name='challenge_protocol.DetectionTracksChallenge.InitializePlanner',
    index=0,
    containing_service=None,
    input_type=_PLANNERINITIALIZATIONLIGHT,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ComputeTrajectory',
    full_name='challenge_protocol.DetectionTracksChallenge.ComputeTrajectory',
    index=1,
    containing_service=None,
    input_type=_PLANNERINPUT,
    output_type=_TRAJECTORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DETECTIONTRACKSCHALLENGE)

DESCRIPTOR.services_by_name['DetectionTracksChallenge'] = _DETECTIONTRACKSCHALLENGE

# @@protoc_insertion_point(module_scope)
