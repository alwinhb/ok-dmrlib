import enum
from typing import Optional, Union, Literal

from okdmr.dmrlib.hytera.pdu.hdap import HDAP, HyteraServiceType
from okdmr.dmrlib.utils.bytes_interface import BytesInterface


@enum.unique
class RCPOpcode(BytesInterface, enum.Enum):
    # [+] Non-standardized services
    UnknownService = 0x0000
    # [+] Call control services
    CallRequest = 0x0841
    CallReply = 0x8841
    RemoveCallRequest = 0x0842
    RemoveCallReply = 0x8842
    PriorityInterruptRequest_MobileAPI = 0x0456
    PriorityInterruptReply_MobileAPI = 0x8456
    BroadcastStatusConfigurationRequest = 0x10C9
    BroadcastStatusConfigurationReply = 0x80C9
    BroadcastTransmitStatus = 0xB843
    BroadcastReceiveStatus = 0xB844
    BroadcastTransmitStatusWithAlias = 0xB84D
    BroadcastReceiveStatusWithAlias = 0xB84E
    BroadcastPopupWindow = 0xB854
    AnalogBroadcastStatusConfigurationRequest = 0x1A00
    AnalogBroadcastStatusConfigurationReply = 0x8A00
    AlertCallWithSenderRequest = 0x0850
    AlertCallWithSenderReply = 0x8850
    EmergencyAlarmWithSenderRequest = 0x0851
    EmergencyAlarmWithSenderReply = 0x8851
    SendTalkerAliasRequest = 0x0852
    SendTalkerAliasReply = 0x8852
    CancelEmergencyAlarmWithSenderRequest = 0x0853
    CancelEmergencyAlarmWithSenderReply = 0x8853
    AnalogBroadcastTransmitReceiveStatus = 0xBA01
    RepeaterBroadcastTransmitStatus = 0xB845
    PriorityInterruptRequest_RepeaterAPI = 0x0457
    PriorityInterruptReply_RepeaterAPI = 0x8457
    XPT_PriorityInterruptRequest = 0x0458
    XPT_PriorityInterruptReply = 0x8458
    XPT_CallSiteBroadcast = 0xBB02
    XPT_HomeGroupListQueryRequest = 0x0B04
    XPT_HomeGroupListQueryReply = 0xBB04
    XPT_StatusBroadcastSubscriptionRequest = 0x1B00
    XPT_StatusBroadcastSubscriptionReply = 0x8B00
    XPT_FreeRepeaterBroadcast = 0xBB01
    CallRequestWithSender = 0x084C
    CallReplyWithSender = 0x884C
    # [-] Call control services
    # [+] Radio control services
    RadioMessageQueryRequest = 0x0201
    RadioMessageQueryReply = 0x8201
    ButtonAndKeyboardOperationRequest = 0x0041
    ButtonAndKeyboardOperationReply = 0x8041
    ZoneAndChannelOperationRequest = 0x00C4
    ZoneAndChannelOperationReply = 0x80C4
    ChannelStatusOrParameterCheckRequest = 0x00E7
    ChannelStatusOrParameterCheckReply = 0x80E7
    ChannelNumberOfZoneRequest = 0x0450
    ChannelNumberOfZoneReply = 0x8450
    RadioCurrentChannelQueryRequest = 0x0134
    RadioCurrentChannelQueryReply = 0x8134
    RadioZoneAliasQueryRequest = 0x0135
    RadioZoneAliasQueryReply = 0x8135
    RadioZoneChangeSubscriptionRequest = 0x1136
    RadioZoneChangeSubscriptionReply = 0x8136
    RadioZoneChangeNotification = 0xB137
    FunctionStatusCheckRequest = 0x00ED
    FunctionStatusCheckReply = 0x80ED
    FunctionEnableDisableRequest = 0x00EE
    FunctionEnableDisableReply = 0x80EE
    InternalExternalSpeakEnableDisableRequest = 0x0045
    InternalExternalSpeakEnableDisableReply = 0x8045
    VolumeCheckControlRequest = 0x0046
    VolumeCheckControlReply = 0x8046
    RadioConfigureOverAirRequest = 0x00C0
    RadioConfigureOverAirReply = 0x80C0
    DeleteSubjectLineTextMessageRequest = 0x0846
    DeleteSubjectLineTextMessageReply = 0x8846
    UpdateAuthenticationKey = 0x0451
    UpdateAuthenticationKeyReply = 0x8451
    RadioIDAndRadioIPQueryRequest = 0x0452
    RadioIDAndRadioIPQueryReply = 0x8452
    ModifyDataServiceRetryTimesRequest = 0x084B
    ModifyDataServiceRetryTimesReply = 0x884B
    RadioSpeakerMuteRequest = 0x0411
    RadioSpeakerMuteReply = 0x8411
    RadioEnableDisableControlRequest = 0x041D
    RadioEnableDisableControlReply = 0x841D
    OperationModeConfigurationRequest = 0x0C10
    OperationModeConfigurationReply = 0x8C10
    RadioCurrentChannelNotificationRequest = 0x1132
    RadioCurrentChannelNotificationReply = 0x8132
    RadioCurrentChannelNotification = 0xB133
    ChannelAliasRequest = 0x0131
    ChannelAliasReply = 0x8131
    RadioConnectLoginRequest = 0x00CA
    RadioConnectLoginReply = 0x80CA
    RadioConnectLogoutRequest = 0x00CB
    RadioConnectLogoutReply = 0x80CB
    StatusChangeNotificationRequest = 0x10C7
    RadioStatusConfigurationReply = 0x80C7
    RadioStatusReport = 0xB0C8
    BroadcastMessageConfigurationRequest = 0x1847
    BroadcastMessageConfigurationReply = 0x8847
    OverTheAirProgrammingRequest = 0x00CC
    OverTheAirProgrammingReply = 0x80CC
    RadioCallSetupModeRequest = 0x0139
    RadioCallSetupModeReply = 0x8139
    PopupWindowQueryRequest = 0x0855
    PopupWindowQueryReply = 0x8855
    # [-] Radio control services
    # [+] Supplementary services
    RadioEnable = 0x084A
    RadioEnableAck = 0x884A
    RadioDisable = 0x0849
    RadioDisableAck = 0x8849
    RadioCheck = 0x0833
    RadioCheckAck = 0x8833
    RemoteMonitor = 0x0834
    RemoteMonitorAck = 0x8834
    AlertCall = 0x0835
    AlertCallAck = 0x8835

    # [-] Supplementary services

    @classmethod
    def _missing_(cls, value: object) -> "RCPOpcode":
        return RCPOpcode.UnknownService

    def as_bytes(self, endian: Literal["big", "little"] = "big") -> bytes:
        return self.value.to_bytes(length=2, byteorder="big")


@enum.unique
class RCPCallType(enum.Enum):
    # common call types
    PrivateCall = 0x00
    GroupCall = 0x01
    AllCall = 0x02
    EmergencyGroupCall = 0x03
    RemoteMonitorCall = 0x04
    EmergencyAlarm = 0x05
    PriorityPrivateCall = 0x06
    PriorityGroupcall = 0x07
    PriorityAllCall = 0x08
    # for repeater only?
    Dispatch = 0x09
    PC = 0x0A
    Alert = 0x0B
    EmergencyAlarmCall = 0x0C
    RadioCheck = 0x0D
    RadioEnable = 0x0E
    RadioDisable = 0x0F


@enum.unique
class RCPResult(enum.Enum):
    Success = 0x00
    Failure = 0x01


@enum.unique
class RepeaterMode(enum.Enum):
    NormalSingleConnection = 0x00
    SelectiveMultiConnection = 0x01


@enum.unique
class RepeaterStatus(enum.Enum):
    LocalRepeating = 0x00
    LocalCallHangTime = 0x01
    IPRepeating = 0x02
    IPCallHangTime = 0x03
    ChannelHangTime = 0x04
    Sleep = 0x05
    RemotePttTx = 0x06
    RemotePttHangTime = 0x07
    RemotePttTxEnd = 0x08
    RemotePttWaitAck = 0x09
    RemotePttTOT = 0x0A
    LocalPttTx = 0x0B
    LocalPttHangTime = 0x0C
    LocalPttTxEnd = 0x0D
    LocalPttWaitAck = 0x0E
    LocalPttTOT = 0x0F


@enum.unique
class RepeaterServiceType(enum.Enum):
    NO_SERVICE = 0x00
    VOICE = 0x01
    TMP = 0x02
    LP = 0x03
    RRS = 0x04
    TP = 0x05
    SUPPLEMENTARY_SERVICE = 0x06
    E2E = 0x07
    """end-to-end encryption repeater data transfer mode"""
    VOICE_OF_PHONE = 0x1F


class RadioControlProtocol(HDAP):
    """
    RCP - Little endian protocol
    """

    def __init__(
        self,
        opcode: Union[bytes, RCPOpcode],
        # unknown service
        raw_payload: bytes = b"",
        raw_opcode: bytes = b"",
        # call request
        call_type: Optional[Union[int, RCPCallType]] = None,
        target_id: Optional[Union[int, bytes]] = None,
        sender_id: Optional[Union[int, bytes]] = None,
        is_reliable: bool = False,
        # call reply
        result: Optional[RCPResult] = None,
        # repeater broadcast transmit status
        repeater_mode: Optional[RepeaterMode] = None,
        repeater_status: Optional[RepeaterStatus] = None,
        repeater_service_type: Optional[RepeaterServiceType] = None,
        # (0x1847)Broadcast Message Configuration Request (Mobile API)
        broadcast_type: int = 0b0000_0111,
    ):
        super().__init__(is_reliable=is_reliable)
        self.opcode: RCPOpcode = RCPOpcode(
            opcode
            if isinstance(opcode, RCPOpcode)
            else int.from_bytes(opcode, byteorder="big")
        )
        # raws
        self.raw_payload: bytes = raw_payload
        self.raw_opcode: bytes = raw_opcode
        #
        self.call_type: Optional[RCPCallType] = (
            RCPCallType(call_type) if isinstance(call_type, int) else call_type
        )
        self.target_id: Optional[int] = (
            target_id
            if (not target_id or isinstance(target_id, int))
            else int.from_bytes(target_id, byteorder=self.get_endianness())
        )
        self.sender_id: Optional[int] = (
            sender_id
            if (not sender_id or isinstance(sender_id, int))
            else int.from_bytes(sender_id, byteorder=self.get_endianness())
        )
        self.result: Optional[RCPResult] = result
        self.repeater_mode: Optional[RepeaterMode] = repeater_mode
        self.repeater_status: Optional[RepeaterStatus] = repeater_status
        self.repeater_service_type: Optional[
            RepeaterServiceType
        ] = repeater_service_type
        self.broadcast_type: int = broadcast_type

    def get_endianness(self) -> Literal["big", "little"]:
        return "little"

    def get_opcode(self) -> bytes:
        if self.opcode == RCPOpcode.UnknownService:
            return self.raw_opcode[0:2]
        return self.opcode.value.to_bytes(length=2, byteorder=self.get_endianness())

    def get_service_type(self) -> HyteraServiceType:
        return HyteraServiceType.RCP

    @staticmethod
    def from_bytes(
        data: bytes, endian: Literal["big", "little"] = "little"
    ) -> Optional["RadioControlProtocol"]:
        (is_reliable, service_type) = HDAP.get_reliable_and_service(data[0:1])
        assert service_type == HyteraServiceType.RCP, f"Expected RCP got {service_type}"

        opcode = RCPOpcode(int.from_bytes(data[1:3], byteorder=endian))
        if opcode == RCPOpcode.UnknownService:
            return RadioControlProtocol(
                opcode=opcode,
                raw_payload=data[5:-2],
                raw_opcode=data[1:3],
                is_reliable=is_reliable,
            )
        elif opcode == RCPOpcode.BroadcastStatusConfigurationRequest:
            return RadioControlProtocol(
                opcode=opcode, raw_payload=data[5:-2], is_reliable=is_reliable
            )
        elif opcode == RCPOpcode.CallRequest:
            return RadioControlProtocol(
                opcode=opcode,
                call_type=data[5],
                target_id=data[6:10],
                is_reliable=is_reliable,
            )
        elif opcode == RCPOpcode.CallReply:
            return RadioControlProtocol(
                opcode=opcode, is_reliable=is_reliable, result=RCPResult(data[5])
            )
        elif opcode == RCPOpcode.RepeaterBroadcastTransmitStatus:
            return RadioControlProtocol(
                opcode=opcode,
                is_reliable=is_reliable,
                repeater_mode=RepeaterMode(int.from_bytes(data[5:7], byteorder=endian)),
                repeater_status=RepeaterStatus(
                    int.from_bytes(data[7:9], byteorder=endian)
                ),
                repeater_service_type=RepeaterServiceType(
                    int.from_bytes(data[9:11], byteorder=endian)
                ),
                call_type=RCPCallType(int.from_bytes(data[11:13], byteorder=endian)),
                target_id=data[13:17],
                sender_id=data[17:21],
            )
        elif opcode == RCPOpcode.BroadcastMessageConfigurationRequest:
            return RadioControlProtocol(
                opcode=opcode, is_reliable=is_reliable, broadcast_type=data[5]
            )
        elif opcode == RCPOpcode.BroadcastMessageConfigurationReply:
            return RadioControlProtocol(
                opcode=opcode, is_reliable=is_reliable, result=RCPResult(data[5])
            )
        else:
            raise ValueError(
                f"Opcode {opcode} (0x{bytes(reversed(data[1:3])).hex().upper()}) not yet implemented"
            )

    def get_payload(self) -> bytes:
        if self.opcode == RCPOpcode.UnknownService:
            # UnknownService is special as it has to keep the original opcode and value untouched
            return self.raw_payload
        elif self.opcode == RCPOpcode.BroadcastStatusConfigurationRequest:
            return (
                # TODO parse to fields and serialize from fields
                self.raw_payload
            )
        elif self.opcode == RCPOpcode.CallRequest:
            return bytes([self.call_type.value]) + self.target_id.to_bytes(
                length=4, byteorder=self.get_endianness()
            )
        elif self.opcode == RCPOpcode.CallReply:
            return self.result.value.to_bytes(1, byteorder=self.get_endianness())
        elif self.opcode == RCPOpcode.RepeaterBroadcastTransmitStatus:
            return (
                self.repeater_mode.value.to_bytes(2, byteorder=self.get_endianness())
                + self.repeater_status.value.to_bytes(
                    2, byteorder=self.get_endianness()
                )
                + self.repeater_service_type.value.to_bytes(
                    2, byteorder=self.get_endianness()
                )
                + self.call_type.value.to_bytes(2, byteorder=self.get_endianness())
                + self.target_id.to_bytes(4, byteorder=self.get_endianness())
                + self.sender_id.to_bytes(4, byteorder=self.get_endianness())
            )
        elif self.opcode == RCPOpcode.BroadcastMessageConfigurationRequest:
            return bytes(
                [
                    # 4 bytes broadcast type
                    0,
                    0,
                    0,
                    self.broadcast_type,
                    # 4 bytes reserved
                    0,
                    0,
                    0,
                    0,
                ]
            )
        elif self.opcode == RCPOpcode.BroadcastMessageConfigurationReply:
            return self.result.value.to_bytes(1, byteorder=self.get_endianness())

        raise ValueError(f"get_payload not implemented for {self.opcode}")

    def __repr__(self):
        represented = f"[RCP.{self.opcode.name}] "
        if self.opcode == RCPOpcode.UnknownService:
            represented += f"[RAW: {self.raw_payload.hex()}]"
        elif self.opcode == RCPOpcode.BroadcastStatusConfigurationRequest:
            represented += f"[Configure {self.raw_payload[0]} broadcast functions]"
        elif self.opcode == RCPOpcode.CallRequest:
            represented += f"[{self.call_type}] [TO: {self.target_id}]"
        elif self.opcode == RCPOpcode.CallReply:
            represented += f"[{self.result}]"
        elif self.opcode == RCPOpcode.BroadcastMessageConfigurationRequest:
            represented += (
                "[BROADCAST "
                + ("NORMAL-TMP " if (self.broadcast_type & 0b1) else "")
                + ("SHORT-DATA " if (self.broadcast_type & 0b10) else "")
                + ("CSBK " if (self.broadcast_type & 0b100) else "")
            ).strip() + "]"
        elif self.opcode == RCPOpcode.BroadcastMessageConfigurationReply:
            represented += f"[{self.result}]"
        elif self.opcode == RCPOpcode.RepeaterBroadcastTransmitStatus:
            represented += (
                f"[RPT MODE: {self.repeater_mode}] [RPT STATUS: {self.repeater_status}] "
                f"[RPT SERVICE: {self.repeater_service_type}] [CALL TYPE: {self.call_type}] "
                f"[SENDER: {self.sender_id}] [TARGET: {self.target_id}]"
            )
        return represented
