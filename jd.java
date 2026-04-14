// VULNERABLE: Direct readObject call
public void deserialize(byte[] data) throws Exception {
    ObjectInputStream ois = new ObjectInputStream(
        new ByteArrayInputStream(data)
    );
    Object obj = ois.readObject(); // B4 vulnerability
}
