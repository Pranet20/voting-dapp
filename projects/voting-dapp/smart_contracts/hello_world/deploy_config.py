import logging

import algokit_utils

logger = logging.getLogger(__name__)


def deploy() -> None:
    # ✅ Correct import: matches generated client
    from smart_contracts.artifacts.hello_world.voting_contract_client import (
        VotingContractClient,
        VotingContractFactory,
    )

    # Create Algorand client from environment (.env)
    algorand = algokit_utils.AlgorandClient.from_environment()

    # Load deployer account from DEPLOYER_MNEMONIC
    deployer = algorand.account.from_environment("DEPLOYER")

    # Create typed factory
    factory = algorand.client.get_typed_app_factory(
        VotingContractFactory,
        default_sender=deployer.address,
    )

    # Deploy the smart contract
    app_client, result = factory.deploy(
        on_update=algokit_utils.OnUpdate.AppendApp,
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
    )

    # Fund the app account if created or replaced
    if result.operation_performed in (
        algokit_utils.OperationPerformed.Create,
        algokit_utils.OperationPerformed.Replace,
    ):
        algorand.send.payment(
            algokit_utils.PaymentParams(
                sender=deployer.address,
                receiver=app_client.app_address,
                amount=algokit_utils.AlgoAmount(algo=1),
            )
        )

    logger.info(
        f"✅ VotingContract deployed successfully | "
        f"App ID: {app_client.app_id} | "
        f"App Address: {app_client.app_address}"
    )
