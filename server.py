from dataclasses import dataclass
from typing import List
import os

from govyn import create_app

@dataclass
class AddRequest:
	numbers: List[int]

@dataclass
class Response:
	result: int

class CalculatorAPI:
	# run initialisation tasks, e.g. connecting to a database
	async def startup(self) -> None:
		pass

	# be a good citizen and dispose of things appropriately
	async def shutdown(self) -> None:
		pass

	# get_ methods take a query string
	# callers will receive a 400 Bad Request if they supply invalid values
	async def get_add(self, a: int, b: int) -> Response:
		'''Add two numbers together'''

		return Response(a + b)

	# post_ methods take a JSON request body
	# also type-checked according to the dataclass definition
	async def post_add(self, req: AddRequest) -> Response:
		'''Add a whole bunch of numbers together'''

		return Response(sum(req.numbers))

app = create_app(CalculatorAPI())
