import os

from dependency_injector import containers, providers
from dotenv import load_dotenv

from application.create_megaverse_use_case import CreateMegaverseMapUseCase
from application.delete_megaverse_use_case import DeleteMegaverseMapUseCase
from domain.repositories.map_repository import MapRepository
from infrastructure.api_map_repository import ApiMapRepository
from infrastructure.astral_object_adapter import AstralObjectAdapter
from infrastructure.common.file_service import FileService
from infrastructure.common.http_client import HttpClient

load_dotenv()


class Container(containers.DeclarativeContainer):
    http_client: HttpClient = providers.Factory(HttpClient)
    astral_object_adapter: AstralObjectAdapter = providers.Factory(AstralObjectAdapter)
    file_service: FileService = providers.Factory(FileService)

    CANDIDATE_ID: str = os.getenv("CANDIDATE_ID")
    GOAL_MAP_URL: str = os.getenv("GOAL_MAP_URL")
    COMETH_URL: str = os.getenv("COMETHS_URL")
    POLYANET_URL: str = os.getenv("POLYANETS_URL")
    SOLOON_URL: str = os.getenv("SOLOONS_URL")

    map_repository: MapRepository = providers.Factory(
        ApiMapRepository,
        http_client=http_client,
        file_service=file_service,
        astral_object_adapter=astral_object_adapter,
        candidate_id=CANDIDATE_ID,
        goal_map_url=GOAL_MAP_URL,
        cometh_url=COMETH_URL,
        polyanet_url=POLYANET_URL,
        soloon_url=SOLOON_URL
    )

    create_megaverse_use_case: CreateMegaverseMapUseCase = providers.Factory(
        CreateMegaverseMapUseCase,
        map_repository=map_repository
    )
    delete_megaverse_use_case: DeleteMegaverseMapUseCase = providers.Factory(
        DeleteMegaverseMapUseCase,
        map_repository=map_repository
    )
