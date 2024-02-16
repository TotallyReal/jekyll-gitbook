require 'base64'
require 'open3'


module Jekyll
  class Environment < Generator
    priority :low

    def generate(site)

      puts "------------------+++++++++++++++++++++++++++----------------"
      
      site.collections["pages"].docs.each do |doc|
        puts "converting #{File.basename(doc.path, '.*')}"
        encoded_text = Base64.strict_encode64(doc.content)
        Open3.popen3("python _scripts\\general_converter.py \"#{encoded_text}\"") do |stdin, stdout, stderr|
          doc.content = stdout.read
        end
      end

      # c = site.collections["pages"]

      # input = c.docs[0].content
      
      # modified_s = `python scripts\\converter.py '#{Base64.strict_encode64(input)}'`
      # c.docs[0].content = modified_s
      # puts modified_s

      puts "--------------------------------------------------------------------"
    end
  end
end

def print_variables(obj)
  puts "# #{obj.class}"
  obj.instance_variables.each do |var|
    var_name = var.to_s.delete('@')
    var_value = obj.instance_variable_get(var)
    var_type = var_value.class
    puts "#{var_name}: #{var_type}"
  end
end

def print_pages()  
  site.pages.each do |page|
    # Print the path and name of the page
    puts "Path: #{page.path}, Name: #{page.name}"
  end
end



