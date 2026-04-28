pub fn brokenFactory() []const u8 {
    return missingGreeting;
}

pub fn brokenConsumer() void {
    _ = brokenFactory();
    _ = missingConsumerValue;
}
