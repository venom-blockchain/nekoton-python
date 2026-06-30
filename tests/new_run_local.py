import asyncio
import os
import nekoton as nt

dirname = os.path.dirname(__file__)


async def main():
    transport = nt.JrpcTransport(endpoint="https://jrpc-new.venom.foundation")
    await transport.check_connection()

    config = await transport.get_blockchain_config()

    account = await transport.get_account_state(
        nt.Address("0:4bc8cc502bb130d5a64a5a291cbd25399923c652d07f1e5cd446f483fe30de26")
    )
    assert account is not None

    configuration_abi = nt.ContractAbi.from_file(
        os.path.join(dirname, "configuration.abi.json")
    )
    details = configuration_abi.function("getDetails").call(account, {}, config=config)
    print(details.output)


if __name__ == "__main__":
    asyncio.run(main())
