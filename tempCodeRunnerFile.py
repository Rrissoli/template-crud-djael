   def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Filme")
        self.assertEquals(type(category.id),UUID)